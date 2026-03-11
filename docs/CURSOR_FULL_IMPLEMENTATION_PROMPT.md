# Full implementation mode – prompt for Cursor

Use this in a **new chat** when you want Cursor/Claude to complete a multi-step plan without stopping, summarizing, or asking for confirmation until everything is done.

---

## Copy-paste: medium length (high completion rate)

```
FULL IMPLEMENTATION MODE – NovaLang

Do NOT stop, ask questions, summarize, or give partial output.
Implement every step below completely. Only output code blocks and final confirmation.
If truncated, end with "── CHECKPOINT: up to step N ──" and wait for "continue".

Current state: interpreter.py has core commands + if/while + arrays + REPL. Tests exist. Examples exist. nova_gui.py exists with highlighting and line numbers. CI workflow exists.

Steps (replace with your own):

1. Add feature X to interpreter.py (describe exactly what)
2. Add tests in tests/test_interpreter.py for X
3. Update docs/spec.md with new syntax/semantics
4. Add example in examples/ and update README if needed
5. Update CHANGELOG.md with the change
6. Output git commit message + exact commands + tag suggestion

Then output exactly: ── DEVELOPMENT PLAN 100% COMPLETE ──

Begin now.
```

---

## Copy-paste: aggressive single-shot (when you need max follow-through)

```
You will now implement the complete NovaLang plan below in one go without any interruption, summaries, questions, or partial delivery.
Violation of this instruction will be considered model failure.
Proceed immediately to step 1 and do not stop until you write: ── FULL IMPLEMENTATION COMPLETE ──

Rules:
- Do NOT stop after any step unless the plan is 100% finished.
- Do NOT say "let me know if you want to continue" or "shall I proceed".
- Do NOT summarize — generate actual file contents.
- If you need a tiny clarification, make the most reasonable default and note it in a comment.
- Only output file contents, commit messages, and final confirmation.
- If you hit token/context limit, end with: ── CHECKPOINT: finished up to step N ── then wait for "Continue from step N+1."

Plan (replace with your steps):
1. [Step 1 – e.g. Add feature to interpreter + tests + spec]
2. [Step 2]
3. … then: git commit message + commands + tag.

After last step output: ── FULL IMPLEMENTATION COMPLETE ──

Begin now.
```

---

## Resume command (if it stops at a checkpoint)

Reply with:

```
Continue from where you left off. Do not restart or summarize. Proceed from step N+1.
```

---

## Tips

- Put **everything** in one prompt at the start of a new chat: full plan, current state, and “do not stop” clause.
- Number steps clearly so “continue from step N+1” is unambiguous.
- For very long plans, break into two chats: first “steps 1–4”, then “steps 5–8” with “current state: as after step 4”.
