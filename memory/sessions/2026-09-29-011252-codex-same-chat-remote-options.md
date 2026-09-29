# Preserve existing chat with remote execution

User specifically wants this existing chat to run off-device. Official remote-connections documentation establishes that existing chats and Git state can be handed to connected hosts with matching saved repositories, using chat footer run-location control. Handoff to Codex cloud is explicitly unsupported, and the calling chat cannot hand itself off via tool. Only local host is advertised in current handoff tool.

Recommendation: configure an always-on destination with matching repository and required runtime/browser, then use UI handoff for this exact chat. OpenAI-hosted Codex cloud requires a cloud task instead; do not promise identical chat migration. SSH projects and mobile Remote have distinct host requirements; phone remote access to a desktop requires that desktop remain awake, online and app running. Browser logins, local resumes, private application ledgers and solver configuration need separate authorized setup; Git-state handoff alone does not provision these.

No new task, host, paid resource or migration created. Source: https://learn.chatgpt.com/docs/remote-connections ; https://learn.chatgpt.com/docs/cloud ; https://learn.chatgpt.com/docs/environments/modes
