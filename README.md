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

There is also an optional separate project-manager companion agent. That agent is not part of the `harnessed` role chain. The user consults it directly when they want project, scope, architecture, or harness-discipline continuity pressure-tested, then carries the resulting correction or decision back into `harnessed`.

## What this repository is for

The harness exists to prevent common failure modes in iterative AI-assisted coding:

* agent momentum silently redefining the project
* local shortcuts becoming permanent architecture
* planning, implementation, and testing collapsing into one blurry step
* approval boundaries disappearing when work touches risky surfaces
* ephemeral chat history being treated as authoritative memory
* theoretical/structural progress being mistaken for live, user-facing behavior

The harness adds structure around those failure modes without turning every small edit into bureaucracy.

## What gets copied where

There are two install surfaces:

1. `harness/` is copied into the target repository.
2. The `.agent.md` files are copied into the client-specific folder where your inference tool loads agent prompts, such as `.copilot/`, `.codex/`, or another tool-specific location.

That split is intentional:

* `harness/` is the repo-local working memory and process scaffold.
* the `.agent.md` files are the agent prompts the client loads.

Typical downstream shape:

```text
your-repo/
  harness/
    1.README.md
    harness-runtime.md
    2.sub-agent-assignment-template.md
    3.sub-agent-roles.md
    4.archive-policy.md
    5.known-failures.md
    6.open-decisions.md
    canon/
      type-system-operational.md
      bridge-schema.md
    implementation-projects/
      active/
      archive/
      templates/
        implementation-plan-template.md
        implementation-tracker-template.md
    project-spec/
      governance-primitives.md
      project-spec.md
```
and 
```text
C:/
  Users/
    user/
      .copilot/        # or .codex/, or another client-specific folder
        agents/
          agent-reference-type-system-canon.md
          coding-harnessed.agent.md
          coding-harness-planner.agent.md
          coding-harness-implementer.agent.md
          coding-harness-reviewer.agent.md
          coding-harness-adversary.agent.md
          coding-harness-archivist.agent.md
```

Add `coding-harness-project-manager.agent.md` if you want a separate continuity check for project intent, scope, architecture, and harness usage.

## Main workflow

Normal use should look like this:

1. The user invokes `coding-harnessed.agent.md`.
2. `coding-harnessed` starts with an ask-first scout pass unless implementation was explicitly authorized.
3. `coding-harnessed` reads the relevant repo-local harness contracts and state.
4. `coding-harnessed` identifies blast radius, approval boundaries, and the smallest coherent change, not smallest mechanical change.
5. `coding-harnessed` delegates bounded work to the relevant role agent when needed.
6. `coding-harnessed` keeps the user in one conversation instead of making them manually coordinate sub-agents.

Optional companion workflow:

1. The user consults `coding-harness-project-manager.agent.md`.
2. The Project Manager pressure-tests project goal, scope, architecture, and drift risk then suggests corrections or next steps.
3. The user carries the useful correction or decision back into `coding-harnessed`.

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
* `project-spec/governance-primitives.md`: project-local governance rules, approval boundaries, and authority distinctions
* `project-spec/project-spec.md`: project-local intent, semantics, architecture, and constraints

### `agents/`

These are the agent definitions you install in the client-specific folder.

| File                                   | Role in the workflow                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `coding-harnessed.agent.md`                   | User-facing orchestrator. Owns the conversation, blast-radius summary, approval boundaries, delegation, and final integration.       |
| `coding-harness-planner.agent.md`             | Internal planning role used by `coding-harnessed` to define seams, non-goals, affected surfaces, approval gates, and verification duties.   |
| `coding-harness-implementer.agent.md`         | Internal implementation role used by `coding-harnessed` to execute one approved seam at a time and validate immediately.                    |
| `coding-harness-reviewer.agent.md`            | Internal review role used by `coding-harnessed` to judge implementation against the plan and verification contract.                         |
| `coding-harness-adversary.agent.md`           | Internal adversarial role used by `coding-harnessed` to stress-test assumptions and propose cheap falsifying checks.                        |
| `coding-harness-archivist.agent.md`           | Internal archival role used by `coding-harnessed` to keep repo-local memory and implementation state coherent.                              |
| `coding-harness-project-manager.agent.md` | Optional separate user-facing companion agent for project and architecture continuity. The user mediates between it and `coding-harnessed`. |
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
* this is not a substitute for project decisions or approval at risky boundaries
* this is not meant to force heavyweight paperwork onto every small edit
* this is not a workflow where the user manually coordinates the internal role agents as peers
* this is not a signal that sub-agents are the point; the point is the contract and the continuity layer

## Summary

This repo packages a portable harness where:

* `harness/` lives in the target repo
* `harness/project-spec/` = authoritative semantic substrate
* the `.agent.md` files live in the client folder
* the user talks to `coding-harnessed`
* `coding-harnessed` operates through harness contracts and repo-local state
* internal role agents are used when needed, but they are not the primary interface
* the optional Project Manager is a separate companion for continuity and drift checking
* verification, approval boundaries, and repo-local memory are part of the workflow rather than afterthoughts
