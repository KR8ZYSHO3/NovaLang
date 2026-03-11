# Next steps (v0.1.1 done – what you can do next)

This doc summarizes what was done for v0.1.1 and what to do locally before releasing.

## Done in this pass

- **REPL** — `python interpreter.py` with no args and no piped stdin → interactive `>>>` prompt; state (variables/arrays) persists. Type `exit`, `quit`, or `:q` to quit; Ctrl+C / Ctrl+D exit gracefully.
- **CI** — `.github/workflows/tests.yml` runs `python -m unittest discover -s tests -v` on push/PR to `main` (Python 3.9–3.12).
- **Version** — Bumped to v0.1.1 in interpreter docstring, README, and `docs/spec.md`.
- **CHANGELOG.md** — Added with v0.1.0 and v0.1.1 entries.

## Before you tag and release

1. **Run tests and examples**
   - `python -m unittest discover -s tests -v`
   - `python interpreter.py examples/hello.nova` (and factorial, array_demo, modulo_demo)

2. **Optional: smoke script**  
   Create `test_all.sh` (or a small Python script) that runs `python interpreter.py examples/*.nova` and checks exit codes.

3. **Branch name**  
   If your default branch is `master`, edit `.github/workflows/tests.yml` and change `branches: [main]` to `branches: [master]`.

## Tag and release

```bash
git add .
git commit -m "v0.1.1: REPL mode, CI workflow, changelog, version bump"
git push -u origin main
git tag v0.1.1
git push origin v0.1.1
```

Then on GitHub: **Releases** → **Draft a new release** → choose tag `v0.1.1` → paste or summarize from CHANGELOG → Publish.

## Later (from DEVELOPMENT.md)

- Improved error messages (line numbers, snippets)
- Runner script (`nova program.nova` or `python -m novalang`)
- More examples and a “Common patterns” tutorial section
- Changelog entry for each future release
