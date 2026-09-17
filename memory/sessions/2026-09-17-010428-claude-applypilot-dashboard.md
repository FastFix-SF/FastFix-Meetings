# ApplyPilot dashboard

- Built a regenerable local status dashboard for the private Sebastian application runs: `dashboard.py` in the private run directory writes `dashboard.html` (self-contained, file://, no network, mode 600). Run `python3 dashboard.py --open` to refresh.
- Reads the existing authoritative outputs only (original-run status CSV, remaining-applications table, `reconcile.py` JSON, batch job/evidence files, CAPTCHA task files); never modifies them. Only receipt-verified rows count as submitted.
- Views: KPI tiles, per-run stacked status bars (click to filter), verified-submissions-per-hour chart, batch tracker with live-worker detection (pgrep on the one-writer guard), "needs a human" table, filterable all-jobs table.
- Snapshot at build time: 58 verified submissions (32 original + 26 additional), 10 already applied, 27 needing applicant input or CAPTCHA drafts, 47 queued, 20 paid CAPTCHA solves; batch-11 worker was live.
- Applicant data stays outside the repository; nothing published. Notion Agent Manager record could not be created (workspace block limit reached).
