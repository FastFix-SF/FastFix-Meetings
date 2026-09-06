# Current State

Last updated: 2026-09-05

## Verified implementation

- Shared repository: FastFix-SF/FastFix-Meetings, default branch main.
- AGENTS.md directs Claude Code and Codex to sync at session start and after
  meaningful work or brainstorming. CLAUDE.md imports AGENTS.md.
- scripts/memory_sync.py supports per-clone enable, sync, status, and disable.
- Sync commits only memory Markdown, integrates teammates' changes, and pushes
  without forcing. Conflicting merges abort while preserving both versions.
- Unrelated staged files are excluded; unpublished non-memory commits block
  publishing. Incoming updates require a clean working tree after saving memory.
- Dated session notes preserve context while the main summaries stay concise.
- README.md includes collaborator setup, recovery, and Sebastian's onboarding prompt.

## Verification

- All 13 local Git integration tests passed, covering two-clone sharing,
  conflicts, offline recovery, scoped commits, rejected pushes, deletions,
  branch/enable guards, symlinks, downloaded folders, and locking.
- The setup was published to GitHub main as commit 663d14d.
- John's downloaded template folder was converted to a proper project clone
  after checking its original files matched the template. Sync is enabled;
  the initial live GitHub sync returned "Memory is up to date."

## Rollout and limitations

- Every collaborator must update their clone and enable sync once with their own
  Git identity, GitHub write access, Git, and Python 3.9+.
- Sebastian's local setup cannot be verified from John's machine.
- This is agent-driven checkpoint syncing, not an always-running background
  service. It depends on agents following instructions and having tool access.
- Product requirements and substantive meeting agenda are still unspecified.
