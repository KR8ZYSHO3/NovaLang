# Pre-public checklist and commands

## Suggested commit message(s)

**Option A — single commit:**
```
Prepare repo for first public release (v0.1)

- README: badge, quick start, Contributing link
- CONTRIBUTING.md: guidelines and dev setup
- examples: add array_demo.nova
- interpreter: minor docstring polish
```

**Option B — two commits:**
```
1) docs: add CONTRIBUTING.md and polish README for public release
2) examples: add array_demo.nova, interpreter docstring tweak
```

---

## Exact git / terminal commands

Run from the repo root (e.g. `c:\Projects\Nova Lang` or `~/NovaLang`):

```bash
# 1. Ensure you're in the repo and on main (or master)
cd "C:\Projects\Nova Lang"
git status

# 2. Stage everything
git add .

# 3. Commit (use one of the messages above)
git commit -m "Prepare repo for first public release (v0.1)"

# 4. Push to GitHub (use 'master' if that's your default branch)
git push -u origin main

# 5. Create and push the first release tag
git tag -a v0.1.0 -m "Initial public release"
git push origin v0.1.0
```

---

## Announcements

**X/Twitter (under 280 characters):**
```
NovaLang v0.1 — a minimal, forgiving language for integer arithmetic. No types, no declarations; undefined vars default to 0 (or 1 for mul). One Python file to run .nova programs. Open source, MIT. https://github.com/KR8ZYSHO3/NovaLang
```

**Reddit / Hacker News (longer):**
```
Title: NovaLang – a minimal, line-based language for integer arithmetic (Python interpreter)

I’ve open-sourced NovaLang, a small imperative language focused on integer arithmetic. It’s designed to be forgiving: variables are created on first use, undefined names default to 0 (or 1 for multiplication), and invalid input becomes 0. One command per line, with set/add/sub/mul/div/mod, print/input, if/while, and sparse arrays. The interpreter is a single Python file with no dependencies (3.7+). I’d love feedback from anyone interested in small languages or interpreters. Repo: https://github.com/KR8ZYSHO3/NovaLang
```

---

## Final checklist before clicking “Make public”

- [ ] README looks good on GitHub (preview with “Preview” or push and view)
- [ ] All links work (spec.md, tutorial.md, examples/, CONTRIBUTING.md, LICENSE)
- [ ] `python interpreter.py examples/hello.nova` runs and prints 42 (or 8)
- [ ] `python -m pytest tests/ -v` (or `python -m unittest discover -s tests -v`) passes
- [ ] LICENSE has correct name (Brandon Shoemaker) and year (2025)
- [ ] No secrets, API keys, or local paths in any file
- [ ] Repo description and topics set (see below)
- [ ] Tag v0.1.0 created and pushed (optional but recommended)

---

## Suggested GitHub repo settings

**Description (one line under repo name):**  
`Minimal, forgiving, line-based language for integer arithmetic. Python interpreter, no deps.`

**Topics/tags:**  
`programming-language`, `interpreter`, `esolang`, `education`, `python`, `language-implementation`, `minimal`

---

## First release tag

**Tag:** `v0.1.0`  
**Message:** `Initial public release`

Command: `git tag -a v0.1.0 -m "Initial public release"` then `git push origin v0.1.0`

---

## Very last step to make the repo public

1. On GitHub, open your repo: **https://github.com/KR8ZYSHO3/NovaLang**
2. Go to **Settings** (tab or gear).
3. Scroll to the **Danger Zone** at the bottom.
4. Click **Change repository visibility**.
5. Choose **Public** and confirm.

After that, the repo is public and the link can be shared.
