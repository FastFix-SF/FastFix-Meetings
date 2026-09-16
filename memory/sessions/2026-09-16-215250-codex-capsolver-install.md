# CapSolver installation — completed

- Request: install core engine first, MCP service, browser extra, and Chromium for this project.
- Used the existing `.venv`; preserved pre-existing `.gitignore` changes and all unrelated files.
- Installed `capsolver-core` 0.1.1 from Git commit `6c6816a933848ea2d136fc47342da4754b1aac49` and `capsolver-mcp` 0.1.1 from `5f1f1f8a5ef95ddf1a66ce3bac0f315f5cfd807a`; browser extra installed Playwright 1.63.0.
- Playwright's Node downloader repeatedly timed out, including a retry with IPv4 preference and a 120-second connection timeout. Downloaded the exact official Chromium and headless-shell archives with curl, extracted into the expected standard cache directories, and reran `python -m playwright install chromium` successfully. Existing FFmpeg was reused.
- Verification: `pip check` passed; imports passed; `capsolver-mcp --help` passed; real MCP stdio initialize/list_tools returned solve_captcha, detect_captchas, solve_on_page, get_balance, get_supported_captchas; local page tests passed in default headless shell and full Chromium, both version 153.0.8010.12.
- Usage from the project directory: `source .venv/bin/activate`, then `capsolver-mcp`. Actual service requests require a CapSolver API key; no credentials were configured or paid API calls made. MCP client registration was not requested.
- No installation work remains. ECC memory tools were unavailable; shared repository memory was used.
