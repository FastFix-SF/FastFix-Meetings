#!/usr/bin/env python3
"""Agent checkpoint sync for memory Markdown. Python 3.9+, Git, no packages."""

import argparse
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


class SyncError(Exception):
    pass


def git(*args, check=True):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_MERGE_AUTOEDIT="no")
    result = subprocess.run(["git", "-C", str(ROOT), *args], env=env,
                            capture_output=True, text=True, timeout=45)
    if check and result.returncode:
        raise SyncError(result.stderr.strip() or result.stdout.strip() or
                        "Git command failed: " + args[0])
    return result


def output(*args):
    return git(*args).stdout.strip()


def config(key):
    return git("config", "--local", "--get", "memorySync." + key,
               check=False).stdout.strip()


def memory_path(name):
    path = PurePosixPath(name)
    return (len(path.parts) > 1 and path.parts[0] == "memory" and
            path.suffix == ".md" and
            all(not part.startswith(".") for part in path.parts))


def names(*args):
    return set(filter(None, git(*args).stdout.split("\0")))


def validate_repo():
    if Path(output("rev-parse", "--show-toplevel")).resolve() != ROOT:
        raise SyncError("This is a downloaded folder, not its own Git clone. Clone the repository first.")
    for name in ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply", "sequencer"):
        path = Path(output("rev-parse", "--git-path", name))
        if (ROOT / path).exists():
            raise SyncError("Finish the existing Git operation before syncing: " + name)
    if output("ls-files", "--unmerged"):
        raise SyncError("Resolve existing conflicts before syncing.")


@contextmanager
def lock():
    path = ROOT / output("rev-parse", "--git-path", "memory-sync.lock")
    try:
        path.mkdir()
    except FileExistsError:
        raise SyncError("Another sync is running. If it crashed, verify no sync process remains, then remove " + str(path))
    try:
        yield
    finally:
        path.rmdir()


def fetch(remote, branch):
    # Keep the ref explicit: never follow a feature branch's upstream by accident.
    git("fetch", "--no-tags", remote,
        "refs/heads/" + branch + ":refs/remotes/" + remote + "/" + branch)


def check_ahead(target):
    # Inspect every commit, including reverted changes and merge parents.
    for commit in output("rev-list", target + "..HEAD").splitlines():
        changed = names("diff-tree", "--root", "-m", "--no-commit-id",
                        "--name-only", "--no-renames", "-r", "-z", commit)
        if any(not memory_path(name) for name in changed):
            raise SyncError("Unpublished changes outside memory Markdown in commit " + commit[:12] +
                            ". Publish/reconcile that work separately before automatic sync.")


def checkpoint():
    changed = (names("diff", "HEAD", "--name-only", "--no-renames", "-z") |
               names("ls-files", "--others", "--exclude-standard", "-z"))
    paths = sorted(name for name in changed if memory_path(name))
    if not paths:
        return
    for name in paths:
        path = ROOT / name
        if any(p.is_symlink() for p in (path, *path.parents)):
            raise SyncError("Memory symlinks cannot be published: " + name)
    # --only excludes unrelated staged files. Explicit paths also include deletions.
    git("--literal-pathspecs", "add", "--", *paths)
    git("--literal-pathspecs", "commit", "--only", "-m", "memory: save shared progress", "--", *paths)
    print("Saved memory checkpoint locally.")


def integrate(target):
    if git("merge-base", "--is-ancestor", target, "HEAD", check=False).returncode == 0:
        return
    # Do not stash or merge over anyone's work, including untracked files.
    if output("status", "--porcelain", "--untracked-files=all"):
        raise SyncError("Incoming updates need a clean working tree. Local work is preserved; "
                        "save/reconcile unrelated edits and rerun sync.")
    result = git("-c", "merge.autostash=false", "-c", "rerere.enabled=false",
                 "merge", "--no-edit", target, check=False)
    if result.returncode:
        conflicts = output("diff", "--name-only", "--diff-filter=U")
        merge_head = ROOT / output("rev-parse", "--git-path", "MERGE_HEAD")
        if merge_head.exists():
            git("merge", "--abort")
        raise SyncError("Could not integrate teammates' updates. Local commits and remote versions "
                        "are preserved. Reconcile the branches and rerun sync.\n" +
                        (conflicts or result.stderr.strip()))


def run_sync():
    if config("enabled") != "true":
        raise SyncError("Run python3 scripts/memory_sync.py enable once in this clone.")
    remote, branch = config("remote"), config("branch")
    if not remote or not branch:
        raise SyncError("Incomplete setup; run enable again.")
    if output("branch", "--show-current") != branch:
        raise SyncError("Automatic memory sync requires branch " + branch + ". Current branch was left unchanged.")
    if output("remote", "get-url", remote) != config("url"):
        raise SyncError("Remote URL changed; review it and run enable again.")
    target = "refs/remotes/" + remote + "/" + branch
    # Save locally even when offline; do not publish until the history check passes.
    checkpoint()
    for attempt in range(3):
        fetch(remote, branch)
        check_ahead(target)
        integrate(target)
        if output("rev-parse", "HEAD") == output("rev-parse", target):
            print("Memory is up to date.")
            return
        result = git("push", "--porcelain", remote, "HEAD:refs/heads/" + branch, check=False)
        if result.returncode == 0:
            print("Memory published to " + remote + "/" + branch + ".")
            return
        # Retry a teammate's competing push, not auth or branch-protection failures.
        if not any(word in result.stdout + result.stderr for word in ("fetch first", "non-fast-forward")):
            raise SyncError("Push failed; local memory is saved.\n" + result.stderr.strip())
    raise SyncError("The remote kept changing. Local memory is saved; rerun sync.")


def enable(remote, branch):
    if remote not in output("remote").splitlines() or remote.startswith("-"):
        raise SyncError("Choose an existing named remote.")
    git("check-ref-format", "--branch", branch)
    if output("branch", "--show-current") != branch:
        raise SyncError("Open a clone on " + branch + " before enabling. No branch was changed.")
    if not output("config", "user.name") or not output("config", "user.email"):
        raise SyncError("Configure your own Git user.name and user.email first.")
    fetch(remote, branch)
    for key, value in {"remote": remote, "branch": branch,
                       "url": output("remote", "get-url", remote), "enabled": "true"}.items():
        git("config", "--local", "memorySync." + key, value)
    print("Enabled agent checkpoint sync for " + remote + "/" + branch +
          ". Run the sync command to check read/write access.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["enable", "sync", "disable", "status"])
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default="main")
    args = parser.parse_args()
    try:
        validate_repo()
        with lock():
            if args.command == "enable":
                enable(args.remote, args.branch)
            elif args.command == "disable":
                git("config", "--local", "memorySync.enabled", "false")
                print("Automatic memory sync disabled for this clone.")
            elif args.command == "status":
                print("enabled=" + (config("enabled") or "false") +
                      " target=" + config("remote") + "/" + config("branch"))
            else:
                run_sync()
    except (SyncError, subprocess.TimeoutExpired, OSError) as error:
        print("Memory sync stopped: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
