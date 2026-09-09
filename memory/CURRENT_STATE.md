# Current State

Last updated: 2026-09-09

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

- September 9 ideation proposal: John wants a company-wide improvement engine that filters external signals against FastFix's actual needs, presents owners a small A/B/C shortlist, and runs selected work through planner/executor/independent-critic repair cycles. His existing GrokBot connections to ChatGPT and Claude are user-reported; the bot runtime and operational access remain unverified.
- Proposed design: two linked stages (evidence-based idea selection, then bounded execution), with zero qualifying ideas allowed, independent tests, and outcome measurement after delivery. Model routing and pilot cadence remain proposals. See the September 9 idea-engine session note for sources and implementation prerequisites.

- September 8 creative demo: `demos/sketch-pursuit/` contains a playable standalone racing-game recreation from John's uploaded reel. Verified driving, traffic collisions, police capture, scoring, nitro, and pause/restart. This uses original Canvas graphics; Viewmax was not installed. See the corresponding session note.

- Every collaborator must update their clone and enable sync once with their own
  Git identity, GitHub write access, Git, and Python 3.9+.
- Sebastian's local setup cannot be verified from John's machine.
- This is agent-driven checkpoint syncing, not an always-running background
  service. It depends on agents following instructions and having tool access.
- Sebastian's planning transcript covers acquisition and funnel work, development QA and feedback handling, template customization, customer data migration, accounting, legal research, grants, spending, collections, and email assistance.
- Proposed task routing: ChatGPT for research, commercial decisions, and financial analysis; Claude Code for implementation and workflow infrastructure; Claude Cowork for document and operational work. These are recommendations, not approved architecture decisions. Preserve working integrations when choosing where a task runs.
