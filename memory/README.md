# Unified Project Memory

These Markdown files are the durable, provider-neutral handoff between Codex
and Claude Code.

- `OPERATING_RULES.md`: working, safety, validation, and handoff rules
- `PROJECT_BRIEF.md`: purpose, users, scope, constraints, and success criteria
- `CURRENT_STATE.md`: verified implementation and project status
- `DECISIONS.md`: durable decisions with brief reasoning
- `NEXT_STEPS.md`: prioritized unfinished work, blockers, and open questions

Keep these files concise. Store durable project context, not chat transcripts.

Use `sessions/` for dated, attributed ideas and outcomes. Run
`python3 scripts/memory_sync.py sync` at session start and after meaningful
checkpoints, following AGENTS.md. Git history preserves previous versions.
