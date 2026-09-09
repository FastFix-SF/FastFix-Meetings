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

- September 9 approved idea-engine handoff: use Grok Bot Personal for FastFix with existing subscription/Claude Code/Codex CLI access and no additional paid usage. Grok discovers X signals; OpenAI and Claude use Agent Reach for research and independent verification. Present zero to three owner choices every three days, then execute selected briefs through the planner/executor/critic loop.
- Created local FASTFIX_IDEA_ENGINE_PLAN.md with the complete build specification and GrokBot setup prompt. Approved Notion destination is a separate FastFix Improvement Engine board below the existing task board in Fastfix Highway. Handoff is ready; GrokBot dispatch, scheduling, research access, and the board still need implementation/verification. No service activated here.

- September 8 creative demo: `demos/sketch-pursuit/` contains a playable standalone racing-game recreation from John's uploaded reel. Verified driving, traffic collisions, police capture, scoring, nitro, and pause/restart. This uses original Canvas graphics; Viewmax was not installed. See the corresponding session note.

- Every collaborator must update their clone and enable sync once with their own
  Git identity, GitHub write access, Git, and Python 3.9+.
- Sebastian's local setup cannot be verified from John's machine.
- This is agent-driven checkpoint syncing, not an always-running background
  service. It depends on agents following instructions and having tool access.
- Sebastian's planning transcript covers acquisition and funnel work, development QA and feedback handling, template customization, customer data migration, accounting, legal research, grants, spending, collections, and email assistance.
- Proposed task routing: ChatGPT for research, commercial decisions, and financial analysis; Claude Code for implementation and workflow infrastructure; Claude Cowork for document and operational work. These are recommendations, not approved architecture decisions. Preserve working integrations when choosing where a task runs.

- September 9 Notion workflow: Fastfix Highway now uses one FastFix Tasks database with Inbox → Plan → Agent loop → Human review → Ready to execute → Done. Views: Workflow, Today, Needs our review, All tasks. Transcript intake in this Codex chat preserves stated owners, infers urgency with reasons, and retains source context. The existing ideation card now has a proposed planning brief (Normal urgency, Today focus, unassigned); Repurpose Recreate remains John-owned and Low, awaiting a brief. No task agents were launched or outcomes published.
- September 9 Wispr export: combined all five available recorded-meeting transcripts whose America/Los_Angeles start dates were September 3–5, 2026 into `Wispr-Flow-Transcripts-2026-09-03-to-2026-09-05.md`. The export was verified complete across paginated transcripts; transcript text was not copied into project memory.
- September 9 transcript review: extracted 70 candidate Notion items from the September 3–5 Wispr transcripts into `Borrador-Ideas-Notion-Transcripciones-2026-09-03-a-05.md`. The list is pending John’s approval, removal, consolidation, assignment, and priority edits. Nothing from the draft was written to Notion.
