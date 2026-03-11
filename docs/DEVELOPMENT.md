# NovaLang development roadmap

What could be done next, roughly by area. Nothing here is mandatory—NovaLang can stay minimal forever. This is a menu of options.

---

## 1. Language features (spec + interpreter)

### High impact, stays minimal

- **Multi-statement `if` / `while` bodies**  
  Right now each `if`/`while` runs exactly one command. Adding a block (e.g. indentation or `begin`/`end`) would allow real factorial/loops without unrolling. Requires a clear block rule in the spec and changes in the interpreter’s line-by-line loop.

- **Chained or multi-op line**  
  Allow one logical “step” to run multiple commands (e.g. `mul fact n; sub n 1` or a dedicated `do ... end`). Eases loops without full blocks.

- **`eq` / `neq` result as value**  
  So you can `set flag 1` when `x eq 5` (e.g. a conditional expression or a `set_if`-style command). Optional but useful for “did condition hold?” without extra variables.

### Medium impact (still integer-focused)

- **Named constants or “no reassign”**  
  Purely optional; could be something like `const name value` that errors on later `set name ...`. Helps readability, not required for v0.1.

- **Comments on same line**  
  Already have line comments (`#`). Could allow `set x 5  # init` if you want; low priority.

### Larger scope (v0.2+)

- **Strings**  
  Literals, `print` of strings, maybe concatenation. Bigger spec and implementation change.

- **Floats**  
  Literals, arithmetic, print. Again a clear spec and interpreter change.

- **Subroutines / functions**  
  e.g. `def name ... end` and `call name` with a simple calling convention. Would need a call stack and possibly local scope.

- **More comparison ops**  
  e.g. `neq` (not equal). Trivial to add; document in spec and add a branch in the interpreter.

---

## 2. Interpreter quality

- **Error messages**  
  Always include line number (you already do for some). Consider column or snippet (e.g. “near `div x 0`”) for clarity.

- **Structured parsing**  
  Right now parsing is mixed with execution. A separate “parse line → command + args” step would make error reporting and future syntax (blocks, multi-statement) easier.

- **No behaviour change**  
  Keep “one command per line” and current semantics; just refactor for clarity and maintainability.

- **Performance**  
  For v0.1, not a goal. If you ever run huge loops or big programs, consider a simple AST and a small bytecode or tree-walk optimizations later.

---

## 3. Tooling and UX

- **REPL**  
  Run `python interpreter.py` with no args and no stdin: read lines, interpret, print results. Great for trying small snippets.

- **`nova` runner script**  
  Optional `nova program.nova` (or `python -m novalang program.nova`) so users don’t have to type `python interpreter.py`. Can be a tiny wrapper or a proper package.

- **Syntax highlighting**  
  `.nova` support in editors (VS Code, etc.) via a simple textmate/grammar or language server. Improves “looks like a real language” feel.

- **Linter / checker**  
  Optional: warn on undefined names (e.g. first use of a name), or on unreachable code. Not required for v0.1.

---

## 4. Documentation and examples

- **Spec**  
  Keep `docs/spec.md` as the single source of truth. When you add a feature, add syntax, semantics, and one small example there first, then implement.

- **Tutorial**  
  `docs/tutorial.md`: add a “common patterns” section (e.g. “loop until zero”, “accumulator”, “array sum”) that match the current single-command `while` limitation.

- **Examples**  
  More small `.nova` programs: gcd, simple “game” (guess number), max of two, etc. Each with a one-line “expected output” comment.

- **Changelog**  
  A simple `CHANGELOG.md` (e.g. “v0.1 – initial release”, “v0.2 – blocks”) so users see what changed.

---

## 5. Testing and CI

- **Tests**  
  You already have a solid unittest suite. For any new feature or command, add at least one test (happy path and one edge case if relevant).

- **CI**  
  GitHub Actions: on push/PR, run `python -m pytest tests/ -v` (or unittest). Ensures nothing breaks when you or others change code.

- **Example smoke tests**  
  Optional: a test that runs each `.nova` in `examples/` and checks stdout against the expected comment. Keeps examples executable and documented.

---

## 6. Repo and community

- **Version tags**  
  You have v0.1.0. For each release (e.g. v0.2.0), tag and optionally add a GitHub Release with a short “What’s new” from the changelog.

- **Contributing**  
  `CONTRIBUTING.md` is in place. As you add features, mention “update spec + tests” so contributors know the workflow.

- **Issues / discussions**  
  Use GitHub Issues for bugs and feature ideas, Discussions for “how should we do X?” so the roadmap stays in one place (e.g. this doc).

---

## Suggested order (if you want to prioritize)

1. **Stabilize v0.1**  
   Fix any bugs, improve error messages, add a few more tests and examples. No new language features.

2. **Tooling**  
   REPL and/or `nova` runner. High impact for little spec change.

3. **Multi-command blocks**  
   Design blocks (or multi-statement lines) in the spec, then implement. Unlocks real loops and conditionals without unrolling.

4. **CI**  
   One workflow that runs tests (and optionally example smoke tests) on push/PR.

5. **Optional**  
   Changelog, more examples, syntax highlighting, then consider strings/floats or subroutines for a future version.

---

Keeping the language minimal is a feature. Everything in this doc is optional; the only “must” for ongoing development is: **update the spec and tests whenever the language or interpreter behaviour changes.**
