"""
Smoke tests for NovaLang: run a few program strings and assert expected output.
Run from project root: python smoke_test.py
Exit code 0 if all pass, 1 otherwise.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from interpreter import interpret


def run(program: str, expected: str, name: str) -> bool:
    try:
        out = interpret(program)
        if out.strip() != expected.strip():
            print(f"FAIL {name}: expected {expected!r}, got {out!r}")
            return False
        print(f"OK   {name}")
        return True
    except Exception as e:
        print(f"FAIL {name}: {e}")
        return False


def main() -> int:
    tests = [
        ("set x 42\nprint x", "42", "set and print"),
        ("add n 10\nprint n", "10", "add undefined (default 0)"),
        ("mul y 5\nprint y", "5", "mul undefined (default 1)"),
        ("set n 5\nset fact 1\nwhile n gt 0 mul fact n sub n 1\nprint fact", "120", "factorial 5"),
    ]
    ok = sum(1 for p, e, n in tests if run(p, e, n))
    total = len(tests)
    print(f"\n{ok}/{total} smoke tests passed.")
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
