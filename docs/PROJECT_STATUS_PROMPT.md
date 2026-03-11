# NovaLang – current project status (paste this to bring Cursor/AI up to speed)

Use this in a new chat when you want the AI to understand exactly where the project is. Copy the section below the line.

---

## NovaLang project context

**What it is:** NovaLang is a minimal, line-based imperative language for integer arithmetic. It is forgiving by design: undefined variables default to 0 (or 1 for `mul`). One command per line; no declarations. Target: teaching, quick math scripts, and a small interpreter codebase.

**Repo:** https://github.com/KR8ZYSHO3/NovaLang (public, `main` branch). MIT © 2025 Brandon Shoemaker.

**Current version:** v0.1.1 (not yet tagged; code is at that level).

### What’s implemented

- **Interpreter** (`interpreter.py`): Single entrypoint `interpret(program, input_fn=None, variables=None, arrays=None) -> str`. All commands: `set`, `add`, `sub`, `mul`, `div`, `mod`, `print`, `input`, `if`, `while`, `array_set`, `array_get`. Multi-command if/while bodies (tokens consumed by arity). Optional `variables`/`arrays` for REPL state.
- **REPL:** Run `python interpreter.py` with no args (and no piped stdin) → interactive `>>>` prompt; state persists. Exit with `exit`, `quit`, or Ctrl+C/Ctrl+D.
- **GUI** (`nova_gui.py`): Tkinter IDE – editor (left) with keyword highlighting and line numbers, output pane (right), toolbar: Run, Clear, New, Open, Save. Run executes editor content via `interpret()`; `input` uses a dialog.
- **CI:** `.github/workflows/tests.yml` runs `python -m unittest discover -s tests -v` on Python 3.9–3.12 on push/PR to `main`.
- **Tests:** `tests/test_interpreter.py` – 16 unit tests (basic ops, defaults, if/while, arrays, errors, input). `smoke_test.py` – 4 quick program strings with expected output.
- **Docs:** `docs/spec.md` (full language spec), `docs/tutorial.md`, `docs/PROJECT_RUNDOWN.md`, `docs/DEVELOPMENT.md` (roadmap), `docs/next-steps.md`, `docs/CURSOR_FULL_IMPLEMENTATION_PROMPT.md` (template for multi-step Cursor prompts). `CHANGELOG.md` has v0.1.0 and v0.1.1.
- **Examples:** `examples/hello.nova`, `factorial.nova`, `array_demo.nova`, `array_sum.nova`, `modulo_demo.nova`.

### Project layout (key files)

```
NovaLang/
├── interpreter.py      # Interpreter + REPL entrypoint
├── nova_gui.py         # Tkinter GUI
├── smoke_test.py       # Smoke tests
├── tests/test_interpreter.py
├── examples/*.nova
├── docs/spec.md, tutorial.md, DEVELOPMENT.md, PROJECT_RUNDOWN.md, ...
├── .github/workflows/tests.yml
├── CHANGELOG.md, CONTRIBUTING.md, LICENSE, README.md
└── .cursor/rules/run-without-permission.mdc  # Run git/terminal without asking
```

### How to run (no install)

- File: `python interpreter.py path/to/file.nova`
- REPL: `python interpreter.py` (no args, no stdin)
- GUI: `python nova_gui.py`
- Tests: `python -m pytest tests/ -v` or `python -m unittest discover -s tests -v`
- Smoke: `python smoke_test.py`

Python 3.7+ required. No dependencies. Tkinter needed for GUI (on some Linux: `python3-tk`).

### What’s not done yet (from DEVELOPMENT.md)

- Strings, floats, `neq`, subroutines
- REPL inside GUI, dark mode, more editor polish
- `nova` runner script, syntax highlighting in editors (e.g. VS Code)
- Changelog/release process (tag v0.1.1, GitHub Release)

When making changes: update `docs/spec.md` and tests when the language or interpreter behavior changes.
