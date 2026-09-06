"""Integration tests against real local Git remotes; no GitHub access."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/memory_sync.py"


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_CONFIG_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0")
        self.remote = self.base / "remote.git"
        self.a, self.b = self.base / "a", self.base / "b"
        self.call(self.base, "git", "init", "--bare", "--initial-branch=main", str(self.remote))
        self.call(self.base, "git", "clone", str(self.remote), str(self.a))
        self.identity(self.a)
        (self.a / "scripts").mkdir()
        shutil.copyfile(SCRIPT, self.a / "scripts/memory_sync.py")
        (self.a / "memory").mkdir()
        (self.a / "memory/state.md").write_text("original\n")
        (self.a / "app.txt").write_text("original app\n")
        self.git(self.a, "add", ".")
        self.git(self.a, "commit", "-m", "initial")
        self.git(self.a, "push", "-u", "origin", "main")
        self.call(self.base, "git", "clone", str(self.remote), str(self.b))
        self.identity(self.b)
        self.sync(self.a, "enable")
        self.sync(self.b, "enable")

    def call(self, cwd, *args, ok=True):
        result = subprocess.run(args, cwd=cwd, env=self.env, text=True,
                                capture_output=True, timeout=20)
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def git(self, cwd, *args):
        return self.call(cwd, "git", *args).strip()

    def identity(self, cwd):
        self.git(cwd, "config", "user.name", "Test Collaborator")
        self.git(cwd, "config", "user.email", "test@example.invalid")

    def sync(self, cwd, command="sync", ok=True):
        return self.call(cwd, sys.executable, "scripts/memory_sync.py", command, ok=ok)

    def test_publish_receive_and_no_empty_commit(self):
        (self.a / "memory/state.md").write_text("shared idea\n")
        self.sync(self.a)
        self.sync(self.b)
        self.assertEqual((self.b / "memory/state.md").read_text(), "shared idea\n")
        head = self.git(self.a, "rev-parse", "HEAD")
        self.sync(self.a)
        self.assertEqual(head, self.git(self.a, "rev-parse", "HEAD"))

    def test_unrelated_staged_file_is_preserved_and_not_pushed(self):
        (self.a / "app.txt").write_text("private local work\n")
        self.git(self.a, "add", "app.txt")
        (self.a / "memory/state.md").write_text("idea\n")
        self.sync(self.a)
        self.assertEqual(self.git(self.a, "diff", "--cached", "--name-only"), "app.txt")
        self.sync(self.b)
        self.assertEqual((self.b / "app.txt").read_text(), "original app\n")

    def test_unpublished_code_commit_blocks_push(self):
        (self.a / "app.txt").write_text("code\n")
        self.git(self.a, "commit", "-am", "unpublished code")
        (self.a / "memory/state.md").write_text("idea\n")
        self.assertIn("outside memory", self.sync(self.a, ok=False))
        self.sync(self.b)
        self.assertEqual((self.b / "memory/state.md").read_text(), "original\n")

    def test_two_collaborators_independent_notes_merge(self):
        (self.a / "memory/john.md").write_text("John's idea\n")
        (self.b / "memory/sebastian.md").write_text("Sebastian's idea\n")
        self.sync(self.a)
        self.sync(self.b)
        self.sync(self.a)
        self.assertTrue((self.a / "memory/sebastian.md").exists())
        self.assertTrue((self.b / "memory/john.md").exists())

    def test_conflict_preserves_both_versions_and_aborts_merge(self):
        (self.a / "memory/state.md").write_text("John's version\n")
        (self.b / "memory/state.md").write_text("Sebastian's version\n")
        self.sync(self.a)
        self.assertIn("preserved", self.sync(self.b, ok=False))
        self.assertEqual((self.b / "memory/state.md").read_text(), "Sebastian's version\n")
        self.assertEqual(self.git(self.b, "show", "origin/main:memory/state.md"), "John's version")
        self.assertFalse((self.b / ".git/MERGE_HEAD").exists())
        self.assertEqual(self.git(self.b, "status", "--porcelain"), "")

    def test_offline_saves_local_checkpoint_and_retries(self):
        hidden = self.base / "offline.git"
        self.remote.rename(hidden)
        (self.a / "memory/state.md").write_text("offline idea\n")
        self.sync(self.a, ok=False)
        self.assertEqual(self.git(self.a, "show", "HEAD:memory/state.md"), "offline idea")
        hidden.rename(self.remote)
        self.sync(self.a)
        self.sync(self.b)
        self.assertEqual((self.b / "memory/state.md").read_text(), "offline idea\n")

    def test_incoming_with_unrelated_work_stops_without_stash(self):
        (self.a / "memory/new.md").write_text("incoming\n")
        self.sync(self.a)
        (self.b / "app.txt").write_text("unfinished\n")
        self.git(self.b, "add", "app.txt")
        self.assertIn("clean working tree", self.sync(self.b, ok=False))
        self.assertEqual((self.b / "app.txt").read_text(), "unfinished\n")
        self.assertEqual(self.git(self.b, "diff", "--cached", "--name-only"), "app.txt")
        self.assertEqual(self.git(self.b, "stash", "list"), "")

    def test_wrong_branch_and_disabled_clone_do_not_commit(self):
        self.git(self.a, "switch", "-c", "feature")
        (self.a / "memory/state.md").write_text("local\n")
        self.assertIn("requires branch main", self.sync(self.a, ok=False))
        self.git(self.a, "switch", "main")
        self.sync(self.a, "disable")
        self.assertIn("enable once", self.sync(self.a, ok=False))
        self.assertEqual(self.git(self.a, "show", "HEAD:memory/state.md"), "original")

    def test_markdown_only_and_symlink_rejection(self):
        (self.a / "memory/private.txt").write_text("do not publish\n")
        (self.a / "memory/new.md").symlink_to(self.a / "app.txt")
        self.assertIn("symlinks", self.sync(self.a, ok=False))
        (self.a / "memory/new.md").unlink()
        (self.a / "memory/new.md").write_text("okay\n")
        self.sync(self.a)
        self.sync(self.b)
        self.assertFalse((self.b / "memory/private.txt").exists())

    def test_deletion_publishes(self):
        (self.a / "memory/state.md").unlink()
        self.sync(self.a)
        self.sync(self.b)
        self.assertFalse((self.b / "memory/state.md").exists())

    def test_download_inside_parent_repo_is_rejected(self):
        nested = self.a / "download"
        (nested / "scripts").mkdir(parents=True)
        shutil.copyfile(SCRIPT, nested / "scripts/memory_sync.py")
        self.assertIn("not its own Git clone", self.sync(nested, "enable", ok=False))

    def test_existing_lock_stops_sync(self):
        (self.a / ".git/memory-sync.lock").mkdir()
        self.assertIn("Another sync", self.sync(self.a, ok=False))

    def test_push_rejected_by_server_preserves_local_memory(self):
        hook = self.remote / "hooks/pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        (self.a / "memory/state.md").write_text("saved locally\n")
        self.assertIn("Push failed", self.sync(self.a, ok=False))
        self.assertEqual(self.git(self.a, "show", "HEAD:memory/state.md"), "saved locally")
        self.sync(self.b)
        self.assertEqual((self.b / "memory/state.md").read_text(), "original\n")


if __name__ == "__main__":
    unittest.main()
