# Agent Harness

Portable repo-local harness for pair coding with explicit blast-radius analysis, bounded sub-agent roles, and working memory that lives in the repo instead of disappearing into chat history.

This repository is a distribution repo. You do not run it as an app or install it as a package. You copy the parts you want into the repo where you want to work.

## What Goes Where

There are two install surfaces in this repo:

1. `harness/` gets copied into the target repo.
2. The `.agent.md` files get copied into the agent-capable dotfolder used by your client, such as `.copilot/`, `.codex/`, or a similar tool-specific location.

That split is intentional:

- `harness/` is repo-local working memory and process scaffolding.
- The `.agent.md` files are client-specific agent definitions.

Typical downstream shape:

```text
your-repo/
  harness/
  .copilot/        # or .codex/, or another client-specific dotfolder
    harnessed.agent.md
    harness-planner.agent.md
    harness-implementer.agent.md
    harness-reviewer.agent.md
    harness-adversary.agent.md
    harness-archivist.agent.md
```

The exact dotfolder and file placement depend on the client you use. The important part is that the `harness/` folder lives with the repo, while the agent definition files live wherever your inference client expects them.

## What This Harness Is For

- keep read-only scouting separate from implementation
- make blast radius and approval boundaries explicit before risky edits
- separate planning, implementation, review, adversarial checking, and archival duties
- require named verification and user-facing acceptance probes for non-trivial work
- keep project memory in files inside the repo instead of relying on chat history
- stay lightweight for small changes while still supporting multi-step work

## Repo Contents

### `harness/`

Portable repo-local working memory and process docs:

- `1.README.md`: orientation for the harness inside a target repo
- `harness-runtime.md`: runtime contract and standing rules
- `2.sub-agent-assignment-template.md`: handoff template for bounded agent work
- `3.sub-agent-roles.md`: role contracts for planner, implementer, reviewer, adversary, and archivist
- `4.archive-policy.md`: when work is complete enough to archive
- `5.known-failures.md`: recurring failure patterns worth detecting early
- `6.open-decisions.md`: current decision authority for still-live choices
- `canon/`: compact claim-discipline references for normal work and higher-risk bridge cases
- `implementation-projects/`: templates plus `active/` and `archive/` state folders for numbered implementation bundles

### `agents/`

Reusable agent definitions:

| File | Purpose |
| --- | --- |
| `harnessed.agent.md` | Main orchestrator for the user conversation. Handles routing, blast radius, approval boundaries, and final integration. |
| `harness-planner.agent.md` | Turns a requested change into an executable plan with seams, checks, and approval gates. |
| `harness-implementer.agent.md` | Executes one approved seam at a time and validates immediately. |
| `harness-reviewer.agent.md` | Reviews diffs against the plan, verification contract, and acceptance probe. |
| `harness-adversary.agent.md` | Tries to falsify assumptions, weak checks, and incomplete reasoning. |
| `harness-archivist.agent.md` | Updates repo-local memory, decisions, failures, and archive state. |
| `bumblebee-product-manager.agent.md` | Optional architecture continuity guardrail for Bumblebee-specific work. |
| `agent-reference-type-system-canon.md` | Shared reference text for the claim-discipline and type-system canon. |

## Core Working Style

This harness assumes a direct, novice-safe workflow:

1. Start with a read-only scout pass unless the user explicitly asks to implement now.
2. Identify the controlling surface and likely blast radius.
3. Define the seam, verification path, and user-facing acceptance probe.
4. Stop for approval before crossing schema, API, auth, storage, deployment, billing, destructive, or broad architecture boundaries.
5. Implement one seam at a time.
6. Review and, when warranted, adversarially test the result.
7. Archive completed implementation memory so later sessions can resume from the repo instead of chat history.

The harness tries hard not to confuse:

- observed evidence
- inference
- unknowns
- proposed action
- validated result

Most of the docs use plain engineering language. The canon files are there when a distinction needs to be sharper, not to force every task into theory language.

## Installation

### 1. Copy the harness into the target repo

Copy the entire `harness/` directory into the root of the repo where you want the workflow to live.

### 2. Copy the agent files into your client dotfolder

Copy whichever `.agent.md` files you want into the dotfolder used by your inference client.

Examples:

- `.copilot/`
- `.codex/`
- another client-specific agent or prompt folder

If you want the full workflow, start with:

- `harnessed.agent.md`
- `harness-planner.agent.md`
- `harness-implementer.agent.md`
- `harness-reviewer.agent.md`
- `harness-adversary.agent.md`
- `harness-archivist.agent.md`

Add `bumblebee-product-manager.agent.md` only if you want the Bumblebee-specific architecture continuity layer.

### 3. Open the target repo and work through the harness

Use the main harnessed agent for normal work, and route to the specialized roles when the task benefits from planning, review, adversarial checking, or archive maintenance.

## Example Prompts

- "Scout this before editing. Tell me the controlling surface, blast radius, unknowns, and the cheapest check that could prove me wrong."
- "Use the harness and implement this now. Stop if the change crosses schema, API, auth, storage, deployment, or other approval boundaries."
- "Review this change against the harness verification contract and lead with findings."
- "Archive this completed implementation and reconcile active, archive, and open-decision state."

## When To Create An Implementation Bundle

For trivial local edits, the harness can stay lightweight.

For multi-step, repo-scoped, risky, or architecture-shaping work, create a numbered bundle under:

```text
harness/implementation-projects/active/
  implementation-XX-plan.md
  implementation-XX-tracker.md
```

When the work is complete, move the bundle into `harness/implementation-projects/archive/` and clean up any still-live references in `harness/6.open-decisions.md`.

## Updating Downstream Repos

Because this repo is copied into other repos, updates are manual by design:

1. Pull the latest changes from this repo.
2. Review what changed in `harness/` and `agents/`.
3. Copy only the pieces you want into the downstream repo and client dotfolder.
4. Avoid blind overwrites if you have customized the harness or agent files locally.

The harness docs and the agent files can be updated independently.

## Non-Goals

- This is not a package manager dependency.
- This is not a hidden-memory agent system.
- This is not a substitute for product decisions or human approval at risky boundaries.
- This is not meant to force heavyweight process onto every one-file change.

## Summary

Use this repo when you want a reusable pair-coding harness that:

- travels across projects
- keeps implementation memory in the repo
- separates roles cleanly
- stays explicit about blast radius, approval boundaries, and verification

Copy `harness/` into the repo you are working in. Copy the `.agent.md` files into your client's dotfolder. Then use the harness to scout, plan, implement, review, and archive work without relying on chat history alone.