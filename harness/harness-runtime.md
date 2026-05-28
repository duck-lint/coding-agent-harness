# Runtime Contract

This document defines the standing behavior for the harness orchestrator and agent roles.

## Runtime Job

- Identify the controlling surface.
- Separate evidence, inference, unknowns, and speculation.
- Identify blast radius before behavior-changing edits.
- Route work to the correct agent.
- Keep verification explicit.
- Separate scaffolding, wiring, and user-facing behavior.
- Keep planning bounded to the current user-authorized implementation goal.
- Update repo-local memory when the project state changes.

## Coherence-First Seams

- Prefer the smallest coherent seam, not the smallest mechanical diff.
- A seam is coherent only if it keeps known dependent fixtures, sample roles, tests, and acceptance probes truthful.
- If the narrowest diff would repurpose an existing fixture or leave a known downstream surface semantically stale, widen additively or escalate.
- Do not call a change "safe" just because it is locally minimal.

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

The active planning horizon is the current user-authorized implementation goal. Sketch contracts only for seams needed to complete that goal or for approval boundaries it touches. Do not preplan future layers, nodes, bundles, phases, or successor implementations unless the user explicitly provides the next end goal.

## Stop Rule

Stop and ask before crossing approval boundaries, widening scope beyond the plan, or making changes whose correctness depends on project intent that is not available in the repo.

## Done Rule

Work is done only when:

- changed surfaces are named
- verification items are pass, fail, blocked, skipped with reason, or deferred with owner
- every behavior-facing claim maps to a passing named acceptance probe or an explicit downgrade to `scaffold-only`, blocked, skipped, or deferred with owner
- remaining risk is explicit
- project memory is updated when relevant
- if an implementation changed state, `harness/implementation-projects/active/`, `harness/implementation-projects/archive/`, and `harness/6.open-decisions.md` are reconciled in the same turn or explicitly marked blocked with owner
- completed implementation bundles are moved out of `active/`; `active/` keeps one live numbered bundle
