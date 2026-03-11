# Move NovaLang into its own repository

If NovaLang is currently a folder inside the "Divine Arsenal" repo, follow these steps to put it in its own repo.

---

## Step 1: Create a new repository on GitHub (you do this in the browser)

1. Go to **https://github.com/new**
2. **Repository name:** `NovaLang` (or another name you prefer, e.g. `NovaLang-Language`)
3. **Description:** `Minimal, forgiving, line-based language for integer arithmetic. Python interpreter.`
4. Choose **Public**.
5. **Do NOT** check "Add a README", "Add .gitignore", or "Choose a license" — you want an **empty** repo.
6. Click **Create repository**.

GitHub will show you a page with the new repo URL, e.g. `https://github.com/KR8ZYSHO3/NovaLang.git` (or a different name if you chose one).

---

## Step 2: Point this project at the new repo and push

Open a terminal in your **Nova Lang** project folder (the one with `interpreter.py`, `nova.py`, etc. at the root) and run the commands below. **Replace `NEW_REPO_URL`** with the URL from Step 1 (e.g. `https://github.com/KR8ZYSHO3/NovaLang-New.git` if you used a different name).

```bash
cd "c:\Projects\Nova Lang"

# Use the new repo as origin (replace NEW_REPO_URL with your new repo URL)
git remote set-url origin NEW_REPO_URL

# Push all branches and tags to the new repo
git push -u origin main
git push origin --tags
```

**Example** (if the new repo is `https://github.com/KR8ZYSHO3/NovaLang.git`):

```bash
git remote set-url origin https://github.com/KR8ZYSHO3/NovaLang.git
git push -u origin main
git push origin --tags
```

---

## If you already have a repo named "NovaLang" and want to replace its contents

If you created `KR8ZYSHO3/NovaLang` earlier and it has the wrong structure (or is empty), you can overwrite it with this project:

```bash
cd "c:\Projects\Nova Lang"
git remote set-url origin https://github.com/KR8ZYSHO3/NovaLang.git
git push -u origin main --force
git push origin --tags --force
```

Use `--force` only if you are sure you want to replace whatever is on GitHub with your local NovaLang. If the current NovaLang repo has the correct content (from our earlier pushes), you don’t need this — just use the repo as is.

---

## After moving

- Set the new repo’s **Description** in About (pencil icon) so it doesn’t show “Divine Arsenal”.
- If you created a **new** repo with a different name, update any links (e.g. in README, docs) from `KR8ZYSHO3/NovaLang` to your new URL.
- Your local folder stays the same; only the `origin` remote and the GitHub repo change.
