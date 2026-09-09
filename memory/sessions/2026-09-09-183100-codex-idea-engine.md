# FastFix company-wide idea engine

## Confirmed objective and context

- John wants a rigorous improvement-idea engine spanning marketing, the platform, automation, and company processes. Owners should receive a small A/B/C shortlist and select work for execution.
- His intended harness is planner → executor → separate critic, with failed checks returning to the planner and then through execution/evaluation again.
- John reports an existing GrokBot connected to ChatGPT and Claude. Its identity, host, durable execution capabilities, and actual integrations are unverified; an optional clarification was requested.
- Used the requested Agent Reach and Visual Explainer skills. The meetings repository is shared planning memory, not the production FastFix application.

## Proposed design, not approved implementation

- Keep the existing bot as the front door if it supports scheduling, persistent job state, model/tool routing, controlled retries, and cost tracking. Otherwise add a small durable runner behind it; avoid choosing a framework before checking current capabilities.
- Separate discovery/selection from execution. Start with a FastFix problem register and internal evidence, then search X, release documentation, repositories, and practitioner evidence for relevant solutions and objections.
- Deduplicate underlying claims, trace original sources, distinguish vendor capability claims from demonstrated FastFix benefit, and compare each candidate with the current approach, a simpler fix, and doing nothing now.
- Hard gates cover relevance, evidence, practical access, economics/maintenance, and a measurable experiment. Rank surviving ideas qualitatively; model agreement and social engagement are not proof. Return zero to three candidates, with rejection reasons and explicit revisit triggers for deferred ideas.
- Provisional roles: Grok with an actual X-search tool for scouting; Agent Reach for retrieval; ChatGPT/OpenAI for business cases; a separate Claude context for critique; Codex/Claude Code for implementation where access exists. Validate routing on the same historical cases before treating any model assignment as best.
- Owner selection approves a bounded brief including objective, scope, permitted actions, costs, acceptance checks, and stop rules. Routine repairs inside that brief continue automatically. Scope/authority changes require a concrete amendment.
- Planner → executor → independent critic repeats with specific evidence-bearing findings. Preserve the approved criteria. Use time/cost/repair caps and no-progress detection; a cap reached is blocked or failed validation, never success.
- Critic acceptance establishes delivery quality. Later outcome monitoring establishes whether the idea actually helped: adopt, adjust, or retire, then feed observed results into future selection.
- Illustrative examples only: funnel measurement, feedback-to-reproduced-regression checks, and failed-automation alerts/replay without duplicate actions. No baselines or ROI were invented and none is a vetted winner.
- Suggested two-week pilot and daily collection/weekly shortlist cadence are proposals, not scheduled tasks. Start one measured experiment with known access; expand after outcomes justify it.

## Verified external evidence

- Inspected the supplied installer and README without executing them. Commit: `1d087406a09b0fcc654ca63a4297c2a84a1d33d8` in `santmun/claude-code-harness`.
- Installer generates one Claude skill and three agent Markdown files. Planner writes SPEC.md once; generator builds/repairs; evaluator independently checks behavior and writes FINDINGS.md. Repairs return directly to generator, not planner.
- It stops after three evaluation passes or when no/only minor issues remain. The pass cap can leave major issues unresolved. It supplies prompt-level workflow instructions, not a durable scheduler or company-wide business filter.
- Source: https://github.com/santmun/claude-code-harness/blob/1d087406a09b0fcc654ca63a4297c2a84a1d33d8/instalar.sh#L33-L60
- Official xAI docs confirm X Search keyword/semantic/user/thread retrieval, date/handle filters, and citations. This verifies a documented capability, not the existing GrokBot deployment.
- Source: https://docs.x.ai/developers/tools/x-search
- As read September 9, xAI announces September 21, 2026 noon PT billing change from $5 per 1,000 calls to $5 per 1,000 posts fetched and $10 per 1,000 profiles fetched. Recheck current prices before implementation and cap search volume as well as tokens.
- Anthropic's engineering guidance supports simple workflows, evaluator/optimizer feedback with clear criteria, environmental ground truth, and stopping conditions: https://www.anthropic.com/engineering/building-effective-agents

## Checks and local state

- Initial memory sync encountered sandbox Git-lock restrictions; rerunning with the standing authorization succeeded and reported up to date.
- ECC memory searches for FastFix and handoff returned no entries. Saved project requirement fact `mem_20260909_2283d095f98d40c9b946` after granting filesystem access to the configured vault.
- Agent Reach doctor ran. Exa search and GitHub retrieval worked. X keyword search returned HTTP 404 on initial attempt and retry; the documented public-account timeline fallback returned three Anthropic posts successfully. Treat keyword discovery as needing repair/replacement, not fully operational. No cookies or credentials were printed or stored in project memory.
- Agent Reach check-update reports installed v1.5.0 is current. No packages or harness were installed.
- Existing untracked demos/ work was preserved.

## Next concrete action

Review the visual proposal, identify GrokBot's runtime and existing permissions, then choose one workflow with a real baseline and define a bounded pilot. No production service, recurring automation, external messaging, deployment, or paid model execution was created in this session.
