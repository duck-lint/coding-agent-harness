# Governance Primitives

This file defines project-local authority, approval, and admissibility rules for harnessed work.

## Authority Order

When sources conflict, resolve them in this order unless the user explicitly says otherwise:

1. Current user instruction.
2. Open decisions in `harness/6.open-decisions.md`.
3. Active implementation plan and tracker.
4. This governance file.
5. Other markdown files under `harness/project-spec/**`.
6. Archived implementation history and prior chat context.

## Approval Boundaries

Require explicit approval before crossing:

- Schema:
- API:
- Auth:
- Storage:
- Deployment:
- Destructive operation:
- Broad architecture:
- Compatibility or fallback commitment:
- Project-intent-dependent behavior not covered by the project spec or current user authorization:

## Project-Spec Alignment

For multi-step, risky, or behavior-facing work, the PM and Planner should ground directives in the project spec by naming:

- Objective:
- Spec basis:
- Applicable invariants:
- Surfaces expected to move:
- Boundaries not authorized:
- Evidence or probe:
- Stop conditions:

If the alignment frame cannot be grounded in this spec, open decisions, active plans, or current user authorization, the work is blocked until the missing authority or clarification is supplied.

## PM Output Validity Condition

A PM recommendation is valid only if all of the following are true:

- Invariants preserved: every invariant named by the project spec, open decisions, or current user instruction remains intact.
- Admissible transformation: every proposed change maps to a transformation or operation the project spec and governance primitives allow.
- No authority escalation: the recommendation does not claim authority the current user instruction, active plan, or open decisions do not grant.
- Traceable surfaces: every surface of change is explicitly traceable to a project-spec constraint, admissible operation, or approved boundary.
- Evidence-backed: every non-trivial claim is backed by an existing probe, a clearly defined next probe, or explicit scaffold-only labeling.

If any condition fails, the PM output must be marked `project-alignment-blocked` and the missing condition must be named.

## Invariants

- Project truths that must remain stable:
- Fixture, sample, or test roles that must remain truthful:
- Compatibility promises, if any:
- Verification duties that must not be skipped:
