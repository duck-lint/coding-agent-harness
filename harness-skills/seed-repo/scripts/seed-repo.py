#!/usr/bin/env python3
"""Seed a repository with the coding harness template."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROLE_FILES = (
    "project-manager.toml",
    "planner.toml",
    "implementer.toml",
    "reviewer.toml",
    "adversary.toml",
    "archivist.toml",
)


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def repo_root_from_skill() -> Path:
    return skill_root().parents[1]


def copy_harness(target: Path, force: bool) -> Path:
    source = skill_root() / "assets" / "repo-harness-template" / "repo-harness"
    destination = target / "harness"

    if not source.is_dir():
        raise SystemExit(f"Template not found: {source}")

    if destination.exists():
        if not force:
            raise SystemExit(f"Refusing to overwrite existing harness: {destination}")
        shutil.rmtree(destination)

    shutil.copytree(source, destination)
    return destination


def install_subagents(source: Path, destination: Path) -> list[Path]:
    if not source.is_dir():
        raise SystemExit(f"Subagents source not found: {source}")

    destination.mkdir(parents=True, exist_ok=True)
    installed: list[Path] = []
    missing: list[str] = []

    for role_file in ROLE_FILES:
        source_file = source / role_file
        if not source_file.is_file():
            missing.append(role_file)
            continue
        target_file = destination / role_file
        shutil.copy2(source_file, target_file)
        installed.append(target_file)

    if missing:
        raise SystemExit("Missing subagent TOMLs: " + ", ".join(missing))

    return installed


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed a repo with the coding harness.")
    parser.add_argument(
        "--target",
        default=".",
        help="Target repository path. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing target harness/ folder.",
    )
    parser.add_argument(
        "--install-subagents",
        action="store_true",
        help="Install harness subagent TOMLs into the Codex agents directory.",
    )
    parser.add_argument(
        "--subagents-source",
        default=None,
        help="Directory containing harness subagent TOMLs. Defaults to this template repo's subagents/ directory.",
    )
    parser.add_argument(
        "--agents-dir",
        default=str(Path.home() / ".codex" / "agents"),
        help="Destination for subagent TOMLs when --install-subagents is used.",
    )

    args = parser.parse_args()
    target = Path(args.target).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)

    harness_path = copy_harness(target, args.force)
    print(f"Seeded harness: {harness_path}")

    if args.install_subagents:
        subagents_source = (
            Path(args.subagents_source).expanduser().resolve()
            if args.subagents_source
            else repo_root_from_skill() / "subagents"
        )
        installed = install_subagents(
            subagents_source,
            Path(args.agents_dir).expanduser().resolve(),
        )
        print("Installed subagents:")
        for path in installed:
            print(f"- {path}")
    else:
        print("Subagents not installed. Install requires explicit approval and --install-subagents.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
