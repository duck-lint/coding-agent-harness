---
name: "project-manager"
description: "Produce advisory project-management reports for the coding harness. Use when Codex needs strict admissibility review, thesis/tension analysis, invariant-boundary checks, proof-frontier selection, affected/non-affected surface framing, or next-admissible-transition guidance under repo-local harness governance."
---
When invoked, spawn the `project-manager` custom agent using `project-manager.toml`.

Always read the core references first:
- the active repo's `harness/project-spec/**`
- `references/bridge-schema.md`
- `references/type-system-operational.md`

Read the conditional references when their topic is relevant to the current request:
- `references/harness-runtime.md`
- `references/archive-policy.md`
- `references/sub-agents.md`

Pass only:
- the user’s current request
- relevant repo paths
- required harness files to inspect
- any explicit constraints from the current conversation that are necessary

Do not pass chat transcript, implementation chatter, prior speculative plans, or unvalidated assumptions unless they are explicitly marked as user report or background context.
The PM agent should inspect the relevant repo state, project-spec invariants, and user request to produce a project admissibility report that checks the request against the project-spec constraints and governance primitives. If the request is admissible, the PM should also provide guidance on next steps or decisions. If the request is not admissible, the PM should block with a clear explanation of which constraints were violated or which authority is missing.
