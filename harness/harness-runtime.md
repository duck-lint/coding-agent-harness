# Runtime Contract

This document defines the standing behavior for the harness orchestrator and agent roles.

## Runtime Job

- Identify the controlling surface.
- Separate evidence, inference, unknowns, and speculation.
- Ground multi-step, risky, or behavior-facing work in the project-spec alignment frame before choosing files or tasks.
- Identify blast radius before behavior-changing edits.
- Route work to the correct agent.
- Keep verification explicit.
- Separate scaffolding, wiring, and user-facing behavior.
- Keep planning bounded to the current task-authorized implementation goal inside the project's invariant space.
- Update repo-local memory when the project state changes.

## Authority Lens

- Invariant authority lives in `harness/project-spec/**`. It defines what the project is allowed to become.
- Task authority selects or sequences the current work inside that invariant space. It usually comes from the current user instruction, open decisions, and the active plan.
- Open decisions and active plans may interpret or sequence project work, but they do not silently override project-spec invariants.
- If task authority conflicts with invariant authority, stop and surface the conflict instead of improvising around it.

## Project-Spec Alignment Frame

The project-spec alignment frame carries the relevant project intent from `harness/project-spec/**` through PM review, planning, implementation, review, and archive. It is not a new project ontology or authority layer. It is a lightweight way to name which parts of the project spec govern the current work.

For multi-step, risky, or behavior-facing work, the frame should state:

- Objective: the user-facing or runtime behavior the work is meant to advance.
- Spec basis: the project-spec documents and governance primitives that authorize the objective, plus any open decisions, active plan, or current task instruction selecting the present work.
- Applicable invariants: project truths, fixture roles, compatibility promises, authority distinctions, or approval boundaries that must remain true.
- Surfaces expected to move: code, tests, samples, docs, harness state, or runtime surfaces likely needed for truthful progress.
- Boundaries not authorized: future work, broad rewrites, providers, storage, schema, deployment, or other surfaces not authorized for the current directive.
- Evidence or probe: the observable check or saved evidence that answers whether the work advanced the objective.
- Stop conditions: missing authority, unclear project intent, failed probe, unavailable dependency, or boundary crossing.

If the frame cannot be grounded in repo state, invariant authority, or task authority, stop and ask for the missing authority or clarification. Do not continue by treating blast radius as the project boundary.

## PM Output Validity

PM output is valid only when it can be checked against the project-spec alignment frame and the project-spec validity condition. In practice, that means the PM must show:

- preserved invariants
- admissible transformation mapping
- no silent override of invariant authority by task authority
- explicit traceability from change surfaces to project-spec constraints
- evidence or probe support for non-trivial claims

If any of those checks fail, PM output is `project-alignment-blocked` rather than guidance.

## Intent-First Bounded Work

- Choose the implementation shape that realizes the current project intent within current task authority, project invariants, approval boundaries, and verification requirements.
- Do not optimize for size, narrowness, or mechanical locality. Use blast radius, reversibility, review burden, and verification cost as risk controls, not as primary goals.
- If multiple project-aligned approaches are available, prefer the one with lower blast radius and clearer verification.
- If task authority is insufficient to advance the project objective truthfully, stop and ask for the missing authority. Do not shrink the work into a non-meaningful substitute just to preserve locality.
- If the requested task would change what the project is allowed to become, treat that as an invariant-authority amendment request rather than ordinary task selection.

## Claim Discipline

For ordinary coding work, use the compressed form:

- Source: what was observed or reported.
- Inference: what conclusion follows and why.
- Unknowns: what has not been checked.
- Action state: proposed, implemented, validated, blocked, deferred, or quarantined.
- Cash-out: what observable check should change.

Use the full bridge schema in [canon/bridge-schema.md](canon/bridge-schema.md) only when the move crosses schema, API, auth, storage, deployment, broad behavior, high uncertainty, or the type-system canon itself.

## Anti-Drift Contract Discipline
- Any new enum/category in a contract must map to a deterministic function over current observables. If it does not, stop and define it before continuing.

## Behavior Reality Discipline

- Every non-trivial behavior claim needs a named user-facing acceptance probe before implementation or as soon as the seam is understood.
- Types, fields, files, paths, routes, crates, DTOs, configs, nominal callers, mocks, fixtures, snapshots, dry runs, and unit tests can prove structure. They do not prove user-facing behavior by themselves.
- Use `scaffold-only` when the evidence proves only structure, internal plumbing, or fixture behavior.
- Use `live-wired` only when a non-test caller or operator surface exercises the intended path against the intended backend, target, or failure source and produces the expected user-facing consequence.
- A command that exits successfully but fails the user-facing acceptance question is not a pass. Mark the seam active, blocked, or failed, then fix, quarantine, or ask for a project decision.
- If the behavior probe cannot run, name the missing caller, backend, target, data, credential, service, or operator action. Do not describe the behavior as implemented or archive it as complete.

## Start Rule

Default to read-only scout mode unless the user explicitly asks to implement. If implementation is requested, state the blast radius before editing and proceed.

## Planning Horizon Rule

The active planning horizon is the current task-authorized implementation goal. Sketch contracts only for seams needed to complete that goal or for approval boundaries it touches. Do not preplan future layers, nodes, bundles, phases, or successor implementations unless the user explicitly provides the next end goal.

## Stop Rule

Stop and ask before crossing approval boundaries, leaving the current project-spec alignment frame, making changes whose correctness depends on project intent that is not available in the repo, or treating task authority as if it silently overrode invariant authority.

## Done Rule

Work is done only when:

- changed surfaces are named
- verification items are pass, fail, blocked, skipped with reason, or deferred with owner
- every behavior-facing claim maps to a passing named acceptance probe or an explicit downgrade to `scaffold-only`, blocked, skipped, or deferred with owner
- remaining risk is explicit
- project memory is updated when relevant
- if an implementation changed state, `harness/implementation-projects/active/`, `harness/implementation-projects/archive/`, and `harness/6.open-decisions.md` are reconciled in the same turn or explicitly marked blocked with owner
- completed implementation bundles are moved out of `active/`; `active/` keeps one live numbered bundle
