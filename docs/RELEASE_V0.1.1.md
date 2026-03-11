# v0.1.1 release – git commands and GitHub Release text

## 1. Tag and push (run from project root)

```bash
cd "c:\Projects\Nova Lang"
git add .
git status
git commit -m "v0.1.1 release prep: nova runner, GUI polish (Examples, dark mode, friendly errors)"
git push origin main
git tag -a v0.1.1 -m "v0.1.1 – REPL, Tkinter GUI, CI, syntax/line-number polish, nova runner"
git push origin v0.1.1
```

## 2. Create GitHub Release

1. Go to https://github.com/KR8ZYSHO3/NovaLang/releases
2. Click **Draft a new release**
3. **Choose a tag:** select `v0.1.1`
4. **Release title:** `v0.1.1 – REPL, Tkinter GUI, CI, syntax/line-number polish`
5. **Description:** paste the block below.
6. Leave “Set as latest release” checked. Do not attach files (source zip is automatic).
7. Click **Publish release**.

---

## Release description (copy-paste into GitHub Release body)

```markdown
## v0.1.1 – REPL, Tkinter GUI, CI, syntax/line-number polish

- **REPL mode:** run `python interpreter.py` (or `python nova.py`) with no arguments for an interactive `>>>` prompt; variables and arrays persist. Type `exit` or `quit` to quit.
- **Tkinter GUI:** `python nova_gui.py` or `python nova.py gui` – IDE with editor (syntax highlighting, line numbers), output pane, Run/Clear/New/Open/Save, Examples button, dark mode toggle. Friendly error messages for division/modulo by zero.
- **nova runner:** `python nova.py` (REPL), `python nova.py file.nova` (run file), `python nova.py gui` (open GUI). On Unix: `chmod +x nova.py` and symlink as `nova` for a single command.
- **GitHub Actions CI** runs tests on push/PR to `main` (Python 3.9–3.12).
- Multi-command if/while bodies: body tokens consumed by command arity (e.g. `while n gt 0 mul fact n sub n 1`).
- Optional `variables` and `arrays` on `interpret()` for REPL state.
- Smoke test: `python smoke_test.py`.

Requires Python 3.7+. No dependencies. Tkinter needed for GUI (on some Linux: `python3-tk`).
```

---

## One-liner for X/Twitter (optional)

```
NovaLang v0.1.1: REPL, Tkinter IDE (syntax highlight + line numbers + dark mode), nova runner script, CI on GitHub Actions. Minimal integer-arithmetic language. https://github.com/KR8ZYSHO3/NovaLang
```
