# Claude powers inside our own UI — research note

Author: Claude Code (for Sebastian). Date: 2026-09-24 UTC.

## Question

Can we take the capabilities Claude Code has (agent loop, tools, subagents,
skills, MCP) and expose them through a FastFix-owned UI?

## Finding (researched via agent-reach: Exa + GitHub + docs)

Yes. Three layers, decreasing amount of "Claude Code powers" you get for free:

1. **Claude Agent SDK** (`@anthropic-ai/claude-agent-sdk`, `claude-agent-sdk`
   Python). This is Claude Code's engine as a library — it bundles the native
   CLI binary and exposes the same agent loop, built-in tools, subagents,
   skills, plugins, MCP, hooks and permissions. The UI only renders a message
   stream. Relevant hooks for a custom UI:
   - streaming input mode → chat UI, interrupts, queued messages, images
   - `canUseTool` callback → our own approval modal (approve / edit input /
     remember / reject / redirect)
   - `AskUserQuestion` tool → our own clarifying-question cards
   - `SessionStore` adapter → persist transcripts to Postgres/S3 instead of
     local disk
   - OpenTelemetry env vars → traces/metrics for free
2. **Messages API directly** — full control, but we write the agent loop,
   tool dispatch and context management ourselves.
3. **Headless `claude -p --output-format stream-json`** — fastest hack,
   weakest contract. Not recommended for a product.

## Operational constraints (from the SDK hosting docs)

- One subprocess per session; ~1 GiB RAM / 5 GiB disk / 1 CPU as a floor.
  Horizontal scaling = pool of containers + consistent hashing on `sessionId`.
- No top-level session timeout; bound with `maxTurns`.
- Multi-tenant isolation requires `settingSources: []`,
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, per-tenant `cwd` and `CLAUDE_CONFIG_DIR`.
- Token cost dominates infra cost by an order of magnitude.
- Requires an Anthropic API key billed to FastFix. A personal Max/Pro
  subscription is not a license to serve our users.

## Reference implementations worth reading

- `anthropics/claude-agent-sdk-demos`
- `siteboon/claudecodeui` (web/mobile UI over Claude Code sessions)
- `ben-vargas/ai-sdk-provider-claude-code` (Vercel AI SDK provider)

## Status

Proposal / research only. No decision taken, nothing built.

## Open questions

- Which FastFix surface would host this (Meetings, ApplyPilot, idea engine)?
- Does the agent need filesystem/Bash tools, or only MCP + custom tools?
  That choice drives the whole sandboxing and cost story.
