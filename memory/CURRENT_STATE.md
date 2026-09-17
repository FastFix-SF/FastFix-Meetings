# Current State

- ApplyPilot dashboard (September 16): a regenerable local `dashboard.py` → `dashboard.html` in the private Sebastian run directory shows verified submissions, blockers, queue, batch progress, live-worker status, and CAPTCHA spend, reading only the existing reconcile outputs. Private, unpublished. See the September 16 session note.

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

- September 10 refinement: John selected Claude Code for actual FastFix platform implementation, with Codex independently verifying and GrokBot coordinating the planner/executor/critic handoffs. Local FASTFIX_IDEA_ENGINE_PLAN.md now includes this routing plus explicit capability-discovery/retest proposals within the existing opportunity-led track. CLI help confirms non-interactive interfaces, not working GrokBot dispatch; deployment remains unverified.


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

### Application workflow checkpoint
- Application workflow: 32 receipt-verified submissions and 10 previously submitted entries are recorded privately. CAPTCHA/loading retries succeeded. Remaining entries require applicant facts/consent, an available listing, or retrieval of the approved resume for external portals/email. Sensitive details and live handles remain private.

- Application discovery recovery: 767 search records exported, eight further candidates shortlisted for live verification. Prior batch ended in an API DNS failure; recovery process observed live. New submissions remain unverified; private run holds evidence and handoff.

- Expanded application progress: two additional browser receipts verified; 1,156 discovery records exported. Two screening-fact blockers recorded, recovery still live, and next batch prepared. Private reports distinguish verified submissions from queued and unverified outcomes.

- Application continuation: recovery finished with three new receipt-verified submissions; next five-job batch launched and observed live. Two factual blockers remain pending applicant answers. Private queue and report retain exclusions, duplicate checks, and verification evidence.

- Application checkpoint: eight additional submissions independently receipt-verified; next five-job batch launched. Private queue has two factual blockers, 65 queued candidates, and four scope exclusions. Full task remains unfinished.

- Application checkpoint: 13 additional submissions independently verified; six paid CAPTCHA solves recorded for this run. Next five-job batch live, following batch prepared. Full discovery and remaining applications are unfinished; private handoff is authoritative for handles and evidence.

- Application checkpoint: 17 additional submissions independently verified after recovering an API interruption; nine paid CAPTCHA tasks recorded. Next five-job batch active, following batch prepared. Full search and remaining applications unfinished; private handoff contains authoritative handles.

- Application receipt audit: 24 additional submissions independently verified. Last batch exhausted its turn limit; completed applications preserved. Fifty candidates remain queued; private handoff records evidence and next batch. Full task remains unfinished.

- Application continuation: completed five more live candidate checks; no new receipts in that batch. Three drafts/portal blockers and two scope exclusions recorded privately. Four additional candidates queued after duplicate review. Following batch observed live; full task remains unfinished.

- Application checkpoint: 25 additional submissions independently receipt-verified. Following batch reached its turn limit; a targeted recovery was launched and observed live. Corrected an overly conservative account-entry blocker; remaining applications and discovery review are unfinished.

- Application queue review: seven additional project-administration/support candidates queued after reviewing duties; another original-list repost excluded. Recovery process remains live with one draft blocked by CAPTCHA and a subsequent application navigation retry underway. Verified additional submissions remain25.

- Application recovery completed with three actual challenge blockers and no new receipts. Ordinary portal email entry was verified to work; its later profile submission encountered a challenge-loading timeout. Next five-candidate batch launched. Additional verified total remains25; full task unfinished.

- Application checkpoint: 26 additional submissions verified. A subsequent run stopped before browser work with a login error; fresh authentication and request checks succeeded, and the unopened batch was restarted with its failed log preserved. Remaining applications and discovery review are unfinished.

- Application checkpoint: active batch progressed past a temporary loading failure. Two more drafts have factual/consent blockers, and one exact original-list duplicate was skipped. Remaining batch candidates are still processing; verified additional total remains26.

- Application handoff checkpoint: latest batch completed with 26 additional verified submissions. Original saved résumé download independently verified and retained privately. Claude Work target chat located, but sending the continuation was not confirmed because UI controls were inaccessible. Full task unfinished; private recovery handoff is current.

- Claude Work UI restored through normal application-menu quit and restart. Existing continuation message now visibly confirmed received; task resumed. Child CLI authentication remains under diagnosis, distinct from terminal login. Agent Reach found Reddit macOS freeze reports and upstream USER/config-directory Keychain issues; sent read-only diagnostic findings to the existing chat. No approval controls changed; no new verified submission count.

- Claude Work diagnostic update: UI and chat execution restored; application worker remains blocked by child authentication. Deeper diagnostics denied by its approval review. Candidate screening continues; authentication cause remains unconfirmed. No new submissions verified.

- Independent application-queue audit confirmed and removed two additional duplicates: an original-list repost and a syndicated vacancy. Current private report:26 verified additional submissions,58 queued,17 blocked,3 duplicates plus scope exclusions. Claude Work received findings and updated records; worker authentication still blocks new submissions. Full goal unfinished.

- Scope review completed:48 queued jobs remain,26 additional submissions verified,17 blocked. Ten unsuitable additions excluded and two duplicates removed during independent audit and writer review. Claude Work confirms its own CLI auth status loggedIn:false/authMethod:none. Same authentication blocker persisted across three consecutive goal turns; normal interactive authentication is required before submission can resume. Deeper diagnostics and alternate direct-browser execution were rejected by its approval review; no controls changed. Goal unfinished; existing drafts and private recovery handoff preserved.


## 2026-09-16 — Local CapSolver installation

- Installed capsolver-core 0.1.1, capsolver-mcp 0.1.1 with browser extras, and Playwright 1.63.0 in this clone's existing ignored `.venv` (Python 3.14.6). Chromium 153.0.8010.12 and its headless shell are installed in the standard user Playwright cache.
- Verified dependency consistency, package imports, MCP initialization/listing of all five tools, and launches of both Chromium variants. API credentials and MCP client registration were outside this installation request; no paid API call was made.

- Application scope expanded by user to California statewide, Bay Area first, with Codex executing directly. Reopened two geography-only exclusions for later California processing. Current private report26 additional verified submissions,48 queued,19 blocked. Correct Chrome profile observed, but native access became unavailable after user changed window; connected browser extension exposes wrong profile. No applications submitted this turn; awaiting correct browser availability. Private recovery handoff updated.

- Native browser access restored temporarily and intended profile/account verified. First queued listing had a disabled Apply control; no form or submission. Repeated window-change interruptions and a transient screen-capture failure prevent reliable native form work. Private evidence/report now26 verified,47 queued,20 blocked; requested uninterrupted access to intended browser window. Full California goal remains unfinished, Bay Area first.

- Direct browser continuation restored in the authorized profile. One application reached review; action-time terms confirmation is pending, and a separate blank-loading attempt was recorded. No new submission receipts. Private handoff contains current UI state.

- Application checkpoint: one new submission verified from a native browser confirmation; additional-run total27. Private reconciler now supports captured native receipts alongside legacy receipts. A possible same-employer repost is held for requisition verification; next distinct employer application started.

- Application continuation:27 additional submissions verified. Two applications reached final review (one with a CAPTCHA); two drafts need factual answers. Specific confirmations/questions sent; drafts retained in authorized browser. No paid CAPTCHA usage this checkpoint.

- Application checkpoint: two more applications fully submitted and native confirmation receipts verified; additional-run total29. CAPTCHA checkbox completed successfully without paid solving. Further factual blockers asked asynchronously; next dispatcher application underway.

- Application checkpoint: one employer-directed email application sent with visible Gmail confirmation. Final review for another application awaits CAPTCHA confirmation. Employer follow-up emails showed two prior Indeed submissions still require employer-side completion; private report now distinguishes these from completed submissions. Resume/autofill review removed unsupported education and corrected employer-contact permission. Private handoff updated; no paid CAPTCHA use this checkpoint.
