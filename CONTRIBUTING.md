# Contributing to NovaLang

Thanks for your interest in NovaLang. We aim to keep the language **minimal and forgiving** while making the interpreter and docs clear and maintainable.

## How to contribute

1. **Open an issue** — Bug reports, feature ideas, or spec questions. For v0.1 we're focused on stability and clarity rather than new language features.
2. **Send a pull request** — Fix a typo, improve an error message, add a test, or clarify the spec. Keep changes small and focused when possible.

## Guidelines

- **Minimalism** — NovaLang is intentionally small. Propose new commands or syntax in an issue first so we can discuss whether they fit.
- **Tests** — New behavior should come with tests in `tests/test_interpreter.py` (use `unittest`).
- **Docs** — If you change the language or add an example, update `docs/spec.md` and/or `examples/` as needed.
- **Style** — Match existing code style (PEP 8–friendly, clear docstrings, type hints where helpful).

## Development setup

```bash
git clone https://github.com/KR8ZYSHO3/NovaLang.git
cd NovaLang
python -m pytest tests/ -v   # or: python -m unittest discover -s tests -v
```

No virtualenv required for running the interpreter or tests; use one if you prefer.

## Questions

Open a [GitHub Discussion](https://github.com/KR8ZYSHO3/NovaLang/discussions) or an issue if you have questions. Be kind and assume good intent.
