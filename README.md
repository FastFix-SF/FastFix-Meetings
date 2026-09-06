# FastFix Meetings

Shared ideas, decisions, and next steps for John, Sebastian, and collaborators.
Claude Code and Codex read the same Markdown memory and publish updates at useful
checkpoints, including brainstorming. No manual push request is needed each time.

## One-time setup for each collaborator

Accept the repository invitation and use your own GitHub account with write
access. You need Git, Python 3.9+, a Git name/email, and Git authentication (for
example, `gh auth login` then `gh auth setup-git`, or existing SSH credentials).
Do not share credentials. Use a real clone, not a downloaded ZIP folder.

For an existing clone, have your agent preserve local work and integrate the
latest main first. For a new clone:

```bash
git clone https://github.com/FastFix-SF/FastFix-Meetings.git
cd FastFix-Meetings
```

Open the clone in Claude Code or Codex and run once:

```bash
python3 scripts/memory_sync.py enable
python3 scripts/memory_sync.py sync
```

On Windows use `python` or `py -3` if needed. Setup is local to each clone:
a GitHub invitation cannot configure a collaborator's computer. Your agent must
be allowed to run Git/network commands in its app; repository instructions
cannot override app sandbox settings. No background service or global hook is
installed.

## Normal use

1. The agent syncs before reading memory to receive teammates' changes.
2. It records useful ideas, outcomes, decisions, and actions in Markdown.
3. It commits memory locally, fetches and integrates incoming updates, then pushes
   to origin/main.

This is **agent-driven checkpoint sync**, not live co-editing. It works when
Claude Code or Codex follows AGENTS.md; CLAUDE.md imports those instructions.
It does not capture ordinary Claude/ChatGPT web chats, unsaved text, or edits
made after the agent closes. Manual Markdown edits are picked up at the next
checkpoint. No changes means no new commit. Agents summarize context instead of
recording full conversations.

## Memory layout

- `memory/PROJECT_BRIEF.md`: purpose, scope, and success criteria.
- `memory/CURRENT_STATE.md`: concise verified status.
- `memory/DECISIONS.md`: approved decisions and rationale.
- `memory/NEXT_STEPS.md`: actions and open questions.
- `memory/sessions/`: dated notes for ideas and session outcomes.
- `memory/OPERATING_RULES.md`: evidence, privacy, and handoff rules.

Keep main summaries short and put history in dated session notes. Label ideas as
proposals until approved. Never record credentials, sensitive customer data, or
full transcripts. Everyone with repository read access can read its memory and
Git history.

## If sync stops

The agent reports the reason. Offline/authentication failures leave memory saved
locally for a later retry. Conflicting merges are aborted; both committed
versions remain available. The agent can reconcile the versions and rerun sync,
asking you when a decision is ambiguous.

Incoming updates require a clean working tree after saving memory. Unrelated
staged files are excluded from memory commits; unpublished commits touching
other files block automatic publishing. The helper does not stash, force-push,
switch branches, discard work, or bypass branch protection. If main requires
pull requests, use that review workflow; direct pushes will report the restriction.
Prefer a dedicated meetings clone on main.

```bash
python3 scripts/memory_sync.py status
python3 scripts/memory_sync.py sync
python3 scripts/memory_sync.py disable
```

Disabling persists until you request re-enabling. If a process crashes, verify
that no sync is running before removing only the `memory-sync.lock` directory
inside the Git directory. Use one writing agent per clone. Teammates can use
separate clones concurrently.

## Prompt for Sebastian or another collaborator

```text
Update my FastFix Meetings clone from https://github.com/FastFix-SF/FastFix-Meetings.
Inspect Git state and preserve all local work. Fetch origin and integrate the
latest main without force-pushing or discarding changes. Resolve straightforward
conflicts while preserving both people's contributions. Read the updated
AGENTS.md and README.md. Check my Git identity and GitHub access, enable automatic
memory sync with python3 scripts/memory_sync.py enable, then run its sync command.
From now on, sync at session start and save and publish concise memory after each
meaningful discussion or work checkpoint, including brainstorming. I authorize
routine memory-only commits and pushes without asking each time. Read the shared
memory and summarize the current state and next steps. Tell me if anything blocks
setup or publishing.
```

## Verification

Run `python3 -m unittest discover -s tests -v`. Tests use temporary local Git
repositories and two collaborator clones; they never contact GitHub.

Git references: [path-scoped commits](https://git-scm.com/docs/git-commit) and
[merges and recovery](https://git-scm.com/docs/git-merge).
