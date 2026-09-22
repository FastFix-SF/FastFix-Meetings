# ApplyPilot scheduling while personal computer is off

User requested research, not deployment or a paid purchase. Used Agent Reach workflow: doctor, Exa search through mcporter, upstream GitHub README/source, and provider pricing. Exa later rate-limited and Jina anonymous reader rejected requests; direct public vendor pages remained readable. Reddit search returned an author self-report, not independently verified operational evidence.

Proposal: a persistent Linux VPS with one browser worker, durable job database/profile/resume, scheduler, restart handling, duplicate prevention and exception reporting. DigitalOcean published 4 GiB/2 vCPU basic plan is $24/month, 8 GiB/4 vCPU $48/month; these are hosting only. One-worker 4 GiB starting size is an estimate requiring a pilot. Upstream ApplyPilot documents headless and continuous operation; standard submission launcher invokes Claude Code. OpenAI support elsewhere does not establish a ChatGPT submission backend.

Alternative: managed cloud browser such as Browserbase (published Developer plan $20/month, 100 browser hours) plus runtime/scheduler integration. It is not a demonstrated drop-in replacement for this local ApplyPilot installation. Separate always-on home computer also works but depends on home power/network. GitHub Actions is a poor first choice for persistent authenticated browser sessions: scheduling may delay/drop and hosted jobs have six-hour limit.

Cloud execution removes dependence on personal laptop uptime, not unresolved applicant facts, MFA, consent or every CAPTCHA. New host should be signed in separately; do not assume macOS encrypted browser cookies migrate to Linux. Preserve private submitted-job ledger to prevent duplicates. No infrastructure provisioned, migration, scheduled task, credential transfer or spending performed.

Sources: https://github.com/Pickle-Pixel/ApplyPilot ; https://www.digitalocean.com/pricing/droplets ; https://www.browserbase.com/pricing ; https://docs.github.com/en/actions/reference/limits ; https://docs.github.com/en/actions/how-tos/troubleshoot-workflows
