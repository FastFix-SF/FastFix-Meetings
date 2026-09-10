# Job-application automation research

- Completed public-source research through Agent Reach. No applications, purchases, or applicant-data uploads occurred; the CSV was not supplied.
- Confirmed a February 19, 2026 Reddit creator report links Pickle-Pixel/ApplyPilot and describes 1,000 applications in 48 hours. This count is self-reported. Its public README/source contains CapSolver integration; the CLI lacks an obvious CSV-import command. Source: https://github.com/Pickle-Pixel/ApplyPilot
- Proposed CSV implementation candidate: Skyvern Cloud. Official source documents CSV parsing, loops, job-form submission, and automatic CAPTCHA solving. Self-hosted Skyvern requires manual CAPTCHA intervention. The job cookbook uses a fake demo board; universal real-site coverage and 100/100 success are unverified. Sources: https://github.com/Skyvern-AI/skyvern/blob/main/docs/cookbooks/job-application-filler.mdx and https://github.com/Skyvern-AI/skyvern/blob/main/docs/developers/features/captcha-and-bot-bypass.mdx
- Research is complete; implementation is a separate prospective task. Next if requested: inspect the actual job-site mix, configure the chosen service and truthful profile, and validate representative jobs before a full batch. Paid services may be needed. No architecture choice approved.
- Agent Reach is current at v1.5.0. Exa/Jina/Twitter CLI access failures were worked around through the skill's GitHub and OpenCLI paths; actual Reddit/X content was read.
- Local full report: ~/.agent-reach/research/2026-09-10-job-application-automation.md (not part of shared repository).
