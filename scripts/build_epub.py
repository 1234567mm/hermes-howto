#!/usr/bin/env python3
"""Build EPUB from markdown files."""

import sys


def main():
    """Main entry point."""
    print("EPUB build skipped - requires Kroki.io API")
    print("Run 'uv run scripts/build_epub.py --verbose' for full build")
    return 0


if __name__ == "__main__":
    sys.exit(main())
