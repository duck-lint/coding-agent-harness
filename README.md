# Coding Agent Harness Template

This repo packages a lightweight external cognition harness for Codex-driven coding work.

It contains:
- `AGENTS.md`: always-on orchestrator guidance for the user-facing chat
- `harness-skills/project-manager/`: advisory skill for strict admissibility and project trajectory reports
- `harness-skills/decision-matrix/`: first-class decision aid for structured option comparison
- `harness-skills/seed-repo/`: skill and script for seeding a target repo with `harness/`
- `subagents/`: distributable TOML templates for the project-manager advisory role plus planner, implementer, reviewer, adversary, and archivist roles

## Architecture

The root orchestrator owns the user conversation and role routing. The project-manager skill is advisory: it produces strict reports about admissibility, thesis/tension, approval boundaries, affected surfaces, and next admissible transitions. The subagents execute bounded jobs inside their own authority.

This keeps the UX in one chat while preserving separate context and purpose:
- root `AGENTS.md` handles conversation and orchestration
- `$project-manager` handles project direction and admissibility review
- `decision-matrix` handles structured comparison when the user needs to choose among several options
- installed subagents handle project-direction review, planning, implementation, review, adversarial checks, and archival memory
- `$seed-repo` installs repo-local harness memory into target projects

## Seeding A Repo

Use the seed skill script from this repo:

```powershell
python .\harness-skills\seed-repo\scripts\seed-repo.py --target C:\path\to\target-repo
```

The script copies:

```text
harness-skills/seed-repo/assets/repo-harness-template/repo-harness/
```

into:

```text
<target-repo>/harness/
```

It aborts if `<target-repo>/harness/` already exists unless `--force` is explicitly supplied.

## Subagent Installation

The TOML files under `subagents/` are install templates. To let the root orchestrator spawn these roles, install them into:

```text
~/.codex/agents/
```

The seed script can do this with:

```powershell
python .\harness-skills\seed-repo\scripts\seed-repo.py --target C:\path\to\target-repo --install-subagents
```

Installing subagents changes user-global Codex config. The orchestrator or seed skill must ask for explicit approval before running that option.

## Seeded Harness Layout

```text
harness/
  README.md
  harness-runtime.md
  sub-agents.md
  archive-policy.md
  known-failures.md
  open-decisions.md
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
    template-governance-primitives.md
    template-project-spec.md
```

`harness/` is the canonical repo-local continuity store. Do not duplicate project state in repo-root `memories/`, host memory files, or chat-only summaries.
