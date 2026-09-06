# Decision Log

## Template decision — Use portable repository memory

**Decision:** Keep durable unified context in tracked Markdown files under
`memory/`, with `AGENTS.md` and `CLAUDE.md` as agent entry points.

**Reasoning:** Codex and Claude Code can read the same repository files without
depending on proprietary chat history or tool-specific automatic memory.

Project-specific decisions should be added below with a date, decision, and
short reasoning.

## 2026-09-05 — Automatically publish shared memory

**Decision:** John authorized automatic memory publishing for collaborators
using Claude Code and Codex, including useful brainstorming progress, without
requiring manual push requests at each checkpoint.

**Reasoning:** Shared context should follow the team across agents and clones.
This standing authorization covers memory; other publishing still needs a request.
