# Unified Project Instructions

This repository uses shared Markdown memory for Claude Code and Codex.

## Start of every session

Run `python3 scripts/memory_sync.py sync` before reading memory. For a new clone,
follow the one-time setup in README.md. Honor an explicit user disable/pause;
never re-enable without their request. If sync fails, report why and treat local
memory as potentially stale; continue independent work without discarding edits.

Read these files in order:

1. `memory/OPERATING_RULES.md`
2. `memory/PROJECT_BRIEF.md`
3. `memory/CURRENT_STATE.md`
4. `memory/DECISIONS.md`
5. `memory/NEXT_STEPS.md`

Read relevant recent `memory/sessions/` notes when deeper context is needed.
Do not load the whole archive by default. Tracked memory is the unified source
of truth ahead of previous conversations or tool-specific automatic memory.

## Save and share progress automatically

After each meaningful checkpoint, including brainstorming with useful ideas,
questions, decisions, or actions even when no code changes:

1. Update CURRENT_STATE.md and NEXT_STEPS.md as needed; avoid rewriting unchanged
   summaries. Update PROJECT_BRIEF.md only when the scope changes.
2. Add only durable, approved decisions to DECISIONS.md.
3. Create/update one note per session in `memory/sessions/` named
   `YYYY-MM-DD-HHMMSS-author-topic.md` (UTC timestamp, short author/topic; add a
   unique suffix if the filename exists). Record outcomes, ideas, open questions,
   and next actions. Label proposals and assumptions clearly.
4. Review memory changes for accuracy and sensitive content, then run
   `python3 scripts/memory_sync.py sync`.
5. Report whether memory was published or saved locally with sync pending.

Do this before the final response and at useful milestones during longer work.
Do not wait for a request to update memory, commit, or push. Skip empty notes for
exchanges with no durable new context. Keep summaries concise; use session notes
for history, not raw transcripts. Never record secrets, credentials, or sensitive
personal/customer data.

## Standing authorization and recovery

The owner authorizes routine commits/pushes of `memory/**/*.md` to the configured
shared branch after one-time setup, for both Claude Code and Codex. Do not ask
for permission at each checkpoint. Preserve user-authored work. Publishing other
files, deploying, and other consequential external actions require a user request.

Never force-push, discard edits, silently choose one person's side of a conflict,
or publish unrelated commits to make sync work. The helper aborts conflicting
merges and preserves both branches. Reconcile both versions using project
context; ask only when their meaning requires a decision. Report unresolved
failures instead of claiming sync succeeded. Use one writing agent per clone;
each collaborator should work in their own clone on the shared branch.
