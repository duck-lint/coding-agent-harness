# Agent Harness

Portable repository for a repo-local AI coding harness.

This is a distribution repo, not an app, package, or runtime service. You copy the harness into the repo you are working on, and you copy the `.agent.md` files into whatever client-specific agent folder your tool uses.

The point of the harness is not “more agents for their own sake.” The point is to keep AI-assisted coding inside explicit contracts: ownership boundaries, approval boundaries, repo-local memory, verification discipline, and a single user-facing entrypoint.

## Core model

The user should talk to one orchestrator:

```text
user → harnessed.agent.md → harness contracts + repo-local state → bounded role agents when needed
```

That is the important shape.

`harnessed.agent.md` is the user-facing orchestrator. The planner, implementer, reviewer, adversary, and archivist are internal roles that `harnessed` may use when the work calls for them. They are not meant to become separate day-to-day entrypoints.

There is also an optional separate product-manager companion agent. That agent is not part of the `harnessed` role chain. The user consults it directly when they want product, scope, architecture, or harness-discipline continuity pressure-tested, then carries the resulting correction or decision back into `harnessed`.

## What this repository is for

The harness exists to prevent common failure modes in iterative AI-assisted coding:

* implementation momentum silently redefining the product
* local shortcuts becoming permanent architecture
* planning, implementation, and review collapsing into one blurry step
* approval boundaries disappearing when work touches risky surfaces
* chat history being treated as authoritative memory
* structural progress being mistaken for live, user-facing behavior

The harness adds structure around those failure modes without turning every small edit into bureaucracy.

## What gets copied where

There are two install surfaces:

1. `harness/` is copied into the target repository.
2. The `.agent.md` files are copied into the client-specific folder where your inference tool loads agent definitions, such as `.copilot/`, `.codex/`, or another tool-specific location.

That split is intentional:

* `harness/` is the repo-local working memory and process scaffold.
* the `.agent.md` files are the agent definitions the client loads.

Typical downstream shape:

```text
your-repo/
  harness/
  .codex/          # or .copilot/, or another client-specific folder
    harnessed.agent.md
    harness-planner.agent.md
    harness-implementer.agent.md
    harness-reviewer.agent.md
    harness-adversary.agent.md
    harness-archivist.agent.md
```

Add `harness-product-manager.agent.md` if you want a separate continuity check for product intent, scope, architecture, and harness usage.

## Main workflow

Normal use should look like this:

1. The user invokes `harnessed.agent.md`.
2. `harnessed` starts with an ask-first scout pass unless implementation was explicitly authorized.
3. `harnessed` reads the relevant repo-local harness contracts and state.
4. `harnessed` identifies blast radius, approval boundaries, and the narrowest safe seam.
5. `harnessed` delegates bounded work to the relevant role agent when needed.
6. `harnessed` keeps the user in one conversation instead of making them manually coordinate sub-agents.

Optional companion workflow:

1. The user consults `harness-product-manager.agent.md`.
2. The product manager pressure-tests product goal, scope, architecture, and drift risk.
3. The user carries the useful correction or decision back into `harnessed`.

## Repo contents

### `harness/`

This is the portable repo-local working memory that gets copied into a target repo.

* `1.README.md`: orientation for harnessed work in this repo
* `harness-runtime.md`: runtime contract and approval boundaries
* `2.sub-agent-assignment-template.md`: handoff format for bounded sub-agent work
* `3.sub-agent-roles.md`: role responsibilities and handoff rules
* `4.archive-policy.md`: when and how completed work moves to archive
* `5.known-failures.md`: recurring harness or repo failure patterns
* `6.open-decisions.md`: decision authority for still-live decisions
* `canon/type-system-operational.md`: compact claim discipline for normal coding work
* `canon/bridge-schema.md`: fuller bridge schema for high-risk or conceptually slippery moves
* `implementation-projects/active/`: the one live numbered implementation bundle, when needed
* `implementation-projects/archive/`: completed numbered implementation bundles
* `implementation-projects/templates/`: plan and tracker templates

### `agents/`

These are the agent definitions you install in the client-specific folder.

| File                                   | Role in the workflow                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `harnessed.agent.md`                   | User-facing orchestrator. Owns the conversation, blast-radius summary, approval boundaries, delegation, and final integration.       |
| `harness-planner.agent.md`             | Internal planning role used by `harnessed` to define seams, non-goals, affected surfaces, approval gates, and verification duties.   |
| `harness-implementer.agent.md`         | Internal implementation role used by `harnessed` to execute one approved seam at a time and validate immediately.                    |
| `harness-reviewer.agent.md`            | Internal review role used by `harnessed` to judge implementation against the plan and verification contract.                         |
| `harness-adversary.agent.md`           | Internal adversarial role used by `harnessed` to stress-test assumptions and propose cheap falsifying checks.                        |
| `harness-archivist.agent.md`           | Internal archival role used by `harnessed` to keep repo-local memory and implementation state coherent.                              |
| `harness-product-manager.agent.md`     | Optional separate user-facing companion agent for product and architecture continuity. The user mediates between it and `harnessed`. |
| `agent-reference-type-system-canon.md` | Shared reference text for claim discipline and type-system language.                                                                 |

## What the harness is supposed to do

The docs in this repo are designed to keep the following things explicit:

* observed evidence
* inference
* unknowns
* proposed action
* validated result
* approval boundaries
* repo-local memory
* archive state

For normal work, the harness should:

* default to a read-only scout pass unless the user explicitly asks to implement now
* make blast radius explicit before behavior-changing edits
* keep the planning horizon bounded to the current user-authorized goal
* stop for approval before crossing risky boundaries
* require explicit verification and named user-facing acceptance probes for non-trivial work
* keep decisions, failures, handoffs, and implementation state in the repo instead of only in chat history
* keep planning, implementation, review, adversarial checking, and archival duties separate without making the user manually coordinate them

## Implementation bundles

For trivial local edits, the harness should stay light and avoid unnecessary project paperwork.

For multi-step, repo-scoped, risky, or architecture-shaping work, create a numbered bundle under:

```text
harness/implementation-projects/active/
  implementation-XX-plan.md
  implementation-XX-tracker.md
```

When the work is complete, the bundle moves to `harness/implementation-projects/archive/`, and any still-live references in `harness/6.open-decisions.md` should be cleaned up in the same closeout.

## Updating downstream repos

Because this repo is meant to be copied into other repos, updates are manual:

1. pull the latest changes from this repo
2. review what changed in `harness/` and `agents/`
3. copy the updated harness docs into the target repo
4. copy the updated agent files into the client folder
5. avoid blind overwrites if you have customized the harness locally

The harness docs and the agent definitions can evolve separately, so downstream repos may choose to take one without immediately taking the other.

## Non-goals

* this is not a package dependency
* this is not a hidden-memory agent system
* this is not a substitute for product decisions or approval at risky boundaries
* this is not meant to force heavyweight paperwork onto every small edit
* this is not a workflow where the user manually coordinates the internal role agents as peers
* this is not a signal that sub-agents are the point; the point is the contract and the continuity layer

## Summary

This repo packages a portable harness where:

* `harness/` lives in the target repo
* the `.agent.md` files live in the client folder
* the user talks to `harnessed`
* `harnessed` operates through harness contracts and repo-local state
* internal role agents are used when needed, but they are not the primary interface
* the optional product manager is a separate companion for continuity and drift checking
* verification, approval boundaries, and repo-local memory are part of the workflow rather than afterthoughts
