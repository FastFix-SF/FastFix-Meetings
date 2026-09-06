# Codex + Claude Code Unified-Memory Template

Use this GitHub template when starting a project that will move between Codex
and Claude Code. Both agents read and update the same tracked Markdown files;
there is no separate synchronization step.

## Start a new project

1. On GitHub, select **Use this template** and then **Create a new repository**.
2. Give the new repository your project's real name.
3. Clone it or open its local folder in Codex.
4. Prompt Codex:

   ```text
   Initialize this new project from the unified-memory template. Inspect the
   repository, ask me only for information you cannot safely infer, fill the
   memory files with confirmed facts, and recommend the first three next steps.
   Do not build the product yet.
   ```

5. When you later use Claude Code, open the same local project folder and run:

   ```bash
   claude
   ```

   Claude Code imports `AGENTS.md` through `CLAUDE.md` and reads the same memory.

## Normal use

The agents are already instructed to update unified memory after substantial
work. You do not need to paste a memory-update prompt after every interaction.
Before an important handoff or before abruptly closing a session, you can use
this optional safeguard:

```text
Update the unified project memory so the other agent can continue immediately.
```

Never place secrets, credentials, or sensitive personal/customer data in the
tracked memory files.
