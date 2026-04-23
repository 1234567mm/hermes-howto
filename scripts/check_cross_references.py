#!/usr/bin/env python3
"""Check cross-references in markdown files."""

import sys
import re
from pathlib import Path


def check_file(path):
    """Check a single markdown file for cross-reference issues."""
    issues = []

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check for broken internal links
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    for text, link in links:
        if link.startswith("#"):
            continue
        if link.startswith("http"):
            continue
        if link.startswith("mailto"):
            continue
        if link.endswith(".md"):
            link_path = Path(path).parent / link
            if not link_path.exists():
                issues.append(f"Broken link in {path}: {link}")

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

    print("Cross-reference check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
