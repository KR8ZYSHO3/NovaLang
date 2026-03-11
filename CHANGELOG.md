# Changelog

## v0.1.1 (upcoming)

- **REPL mode:** run `python interpreter.py` with no arguments for an interactive `>>>` prompt; variables and arrays persist across lines. Type `exit` or `quit` to quit.
- **Tkinter GUI:** `python nova_gui.py` – simple IDE with editor, output pane, Run/Clear/New/Open/Save. Cross-platform (Windows, macOS, Linux; on some Linux install `python3-tk`).
- **GitHub Actions CI** runs tests on push/PR to `main` (Python 3.9–3.12).
- Multi-command if/while bodies: body tokens are consumed by command arity (e.g. `while n gt 0 mul fact n sub n 1` runs both commands each iteration).
- Optional `variables` and `arrays` parameters on `interpret()` for REPL state.
- Smoke test script: `python smoke_test.py` runs a few program strings and asserts expected output.

## v0.1.0 (2025-03 – Initial public release)

- Core arithmetic commands: `set`, `add`, `sub`, `mul`, `div`, `mod`, `print`
- `input` command (reads integer from stdin; invalid input → 0)
- `if` and `while` with single- or multi-command bodies (op: eq, gt, lt, geq, leq)
- Sparse arrays: `array_set`, `array_get`
- Forgiving defaults: undefined variables → 0 (or 1 for `mul`)
- Division/modulo by zero raise `ValueError`
- Line comments with `#`
- Basic unit tests
