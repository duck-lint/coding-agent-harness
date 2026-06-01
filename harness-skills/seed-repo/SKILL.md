---
name: "seed-repo"
description: "Seed the current working directory/repo with the coding harness using a python script. Also offers explicit approval-gated installation of harness subagent TOMLs into `~/.codex/agents`."
---

# Seed Repo

Seed a repository with the external cognition harness.

## Workflow

1. Confirm the target repo path. Default to the current working directory.
2. Execute the script with Python 3 and specify the repository you intend to seed. Run the script from the template's `seed-repo` directory and pass the target repository path. Examples:

- From the template repo (recommended):
	cd harness-skills/seed-repo
	python3 scripts/seed-repo.py --target /path/to/target-repo

- If the script has been copied into the target repo:
	cd /path/to/target-repo
	python3 scripts/seed-repo.py --target .

3. Abort if `<target-repo>/harness/` already exists unless the user explicitly requests `--force`. If the harness already exists the script will abort with a message like "Refusing to overwrite existing harness: <path>" unless `--force` is passed. The script does not currently implement `--backup` or `--dry-run`.
4. Verify the target repo now contains `harness/`, not `repo-harness/` or `repo-harness-template/`.
5. Tell the user that subagent TOMLs are distributable templates and must be installed into `~/.codex/agents` before the root orchestrator can spawn them.
6. Ask for explicit approval before running `scripts/seed-repo.py --install-subagents` because it writes to user-global Codex config.

## Script

Use:

```bash
# From the template repo's seed-repo directory:
cd harness-skills/seed-repo
python3 scripts/seed-repo.py --target /path/to/target-repo

# Or, to seed the current directory when the script is present there:
python3 scripts/seed-repo.py --target .
```

Prerequisites:
- Python 3.8+ should be installed and available on PATH.
- If `scripts/seed-repo.py` is not found at the path you invoke, abort and verify you are running from the template repo's `seed-repo` directory or specify the full path to the script.

Error handling notes:
- If destination `harness/` exists, the script aborts unless `--force` is used; it prints a refusal message and exits non-zero.
- If a copy fails due to permissions or an interruption, the script will exit with a non-zero status. Consider creating a manual backup before running the script, as automatic backup/dry-run flags are not implemented.

Optional flags:
- `--force`: replace an existing target `harness/` folder.
- `--subagents-source /path/to/subagents`: source directory containing `planner.toml`, `implementer.toml`, `reviewer.toml`, `adversary.toml`, and `archivist.toml`.
- `--install-subagents`: copy subagent TOMLs into `~/.codex/agents`. Use only after explicit user approval.

## Guarantees

- Repo seeding writes only to the target repo.
- Subagent installation is separate from repo seeding.
- The script never silently mutates `~/.codex/agents`.
- The seeded harness uses root-level `harness/harness-runtime.md`, `harness/open-decisions.md`, and `harness/known-failures.md`.
