# Unified Project Instructions

This repository uses portable project memory unified across Codex and Claude Code.

Before substantial work, read these files in order:

1. `memory/OPERATING_RULES.md`
2. `memory/PROJECT_BRIEF.md`
3. `memory/CURRENT_STATE.md`
4. `memory/DECISIONS.md`
5. `memory/NEXT_STEPS.md`

Treat tracked Markdown files under `memory/` as the unified source of truth,
ahead of previous conversations or tool-specific automatic memory.

After substantial work:

1. Update `memory/CURRENT_STATE.md` with the verified current state.
2. Add only durable, approved decisions to `memory/DECISIONS.md`.
3. Update `memory/NEXT_STEPS.md` so another agent can continue immediately.
4. Update `memory/PROJECT_BRIEF.md` only when the project scope changes.

Keep memory concise and factual. Clearly distinguish confirmed facts,
assumptions, decisions, open questions, and recommended actions. Never store
passwords, API keys, tokens, credentials, or sensitive personal/customer data
in project memory.

Preserve existing user-authored files and changes. Do not commit, push,
publish, deploy, or take consequential external actions unless the user asks.
