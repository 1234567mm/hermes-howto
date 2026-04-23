#!/usr/bin/env python3
"""Check Mermaid syntax in markdown files."""

import sys
import re
from pathlib import Path


def check_file(path):
    """Check a single markdown file for Mermaid syntax issues."""
    issues = []

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all mermaid blocks
    mermaid_blocks = re.findall(r"```mermaid\n(.*?)```", content, re.DOTALL)

    for i, block in enumerate(mermaid_blocks):
        block = block.strip()
        if not block:
            issues.append(f"Empty mermaid block in {path}")
            continue

        # Basic syntax checks
        if not any(
            block.startswith(kw)
            for kw in [
                "graph",
                "flowchart",
                "sequenceDiagram",
                "classDiagram",
                "stateDiagram",
                "erDiagram",
                "gantt",
                "pie",
                "mindmap",
                "timeline",
            ]
        ):
            issues.append(f"Invalid mermaid diagram type in {path}: {block[:50]}...")

    return issues


def main():
    """Main entry point."""
    md_files = list(Path(".").rglob("*.md"))
    all_issues = []

    for md_file in md_files:
        if ".venv" in str(md_file):
            continue
        issues = check_file(md_file)
        all_issues.extend(issues)

    if all_issues:
        for issue in all_issues:
            print(issue)
        return 1

    print("Mermaid syntax check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
