# Current State

- Simplified Notion workflow (September 9): all 79 FastFix Tasks now use only `To Do`, `In Progress`, or `Done`; urgency uses only `High`, `Medium`, or `Low`. The Today board groups by Stage and displays Task, Owner, Urgency, and Due. The prior review view is now `In Progress`; the archived backlog remains grouped by Stage; the advisor sprint list shows Stage and urgency. Page instructions now explain the three-stage workflow in English. Owners, dates, descriptions, and workstreams were preserved.

- Advisor sprint intake (September 9): extracted a 10-day work program from the Sujay/John/Sebastian meeting into the existing FastFix Tasks database. The prior 48 cards are preserved under `Previous backlog` in the renamed `Archived backlog — Sep 3–5` board. A new `Advisor sprint — Sep 9–19` list contains 30 extracted cards plus one contemporaneous user-created Indeed task, all due September 19. Sprint themes are retention metrics and customer calls, Bay Area revenue, repeatable sales materials and Indeed outreach, priority customer product improvements, secure advisor access, and pausing lower-ROI work. These are reviewable proposals for the advisor, not proof that execution has begun.

- English-only Notion update (September 9): all 48 FastFix Tasks titles and task bodies are now in English, including the two older cards. The native person field is named `Notion Account`; all workflow views keep it hidden and display the name-based `Owner` field. A full fetch scan found no remaining Spanish task text after excluding Sebastián's proper name.

- Owner-field correction (September 9): the visible `Owner` field now uses name tags so John, Sebastián, Alberto, and joint assignments appear. The native Notion person property is preserved as `Cuenta Notion`. All four task views show `Owner` and hide `Cuenta Notion`; 23 approved new cards have named owners and 23 remain intentionally unassigned.

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
- September 9 task approval applied: created 46 cards in FastFix Tasks from the 70-item draft after removals and merges; 48 rows total including the two existing cards. Titles and planning briefs use simple Spanish. 23 new cards have named owners and 23 remain unassigned. Added visible Responsables tags because Sebastián and Alberto are not returned as workspace users; John also retains native Owner assignments. FF-41 grants retained and FF-47 excluded per explicit clarification. FF-61 nightly QA belongs to John, marked Urgent; only the task was created, with no bot launched.
