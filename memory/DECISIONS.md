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

## 2026-09-09 — Transcript task organization
**Decision:** John authorized organizing transcripts supplied in this chat into clear Notion tasks, preserving explicit assignees, deciding urgency, and simplifying the Fastfix Highway board. Work progresses through planning and agent iteration to human review; the team can request rework or choose to publish/execute. Urgency explanations and uncertain details are recorded on cards.
