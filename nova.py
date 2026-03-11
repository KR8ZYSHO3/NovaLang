#!/usr/bin/env python3
"""
NovaLang runner – use: nova (REPL), nova file.nova (run file), nova gui (IDE).
From project root: python nova.py [file.nova | gui | --help]
On Unix you can chmod +x nova.py and symlink/copy as 'nova'.
"""

import os
import sys

# Project root
_ROOT = os.path.dirname(os.path.abspath(__file__))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from interpreter import interpret, repl


def _run_file(path: str) -> None:
    if not os.path.isfile(path):
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()
    try:
        result = interpret(code)
        if result:
            print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def _run_gui() -> None:
    from nova_gui import main
    main()


def _usage() -> None:
    print(__doc__.strip())
    print()
    print("Usage:")
    print("  python nova.py                  # REPL")
    print("  python nova.py file.nova        # run file")
    print("  python nova.py gui              # open GUI IDE")
    print("  python nova.py --help  /  -h    # this help")


def main() -> None:
    if len(sys.argv) == 1:
        repl()
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg in ("gui", "ide"):
            _run_gui()
        elif arg in ("--help", "-h"):
            _usage()
        else:
            _run_file(arg)
    else:
        print("Too many arguments. Use python nova.py --help", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
