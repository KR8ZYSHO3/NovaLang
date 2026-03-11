# NovaLang

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Tests](https://github.com/KR8ZYSHO3/NovaLang/actions/workflows/tests.yml/badge.svg)](https://github.com/KR8ZYSHO3/NovaLang/actions/workflows/tests.yml) **v0.1.1**

**A minimal, forgiving, line-based imperative language for integer arithmetic.**  
No declarations, no types—just variables that default to zero (or one for multiplication). Write a `.nova` file and run it with a single Python script.

## Quick start

```bash
git clone https://github.com/KR8ZYSHO3/NovaLang.git
cd NovaLang
python nova.py examples/hello.nova         # run a file (or: python interpreter.py ...)
python nova.py                             # REPL (>>> prompt)
python nova.py gui                         # GUI editor + Run (or: python nova_gui.py)
```

**Your first program** — save as `greet.nova`:

```
set x 42
print x
```

Run: `python interpreter.py greet.nova` → prints `42`.

## Features

- **Integers only** (v0.1) — no floats, strings, or booleans yet
- **Forgiving defaults** — undefined variables are `0` everywhere except in `mul`, where they're `1` (so `mul x 5` gives `x = 5`)
- **Dynamic variables** — alphanumeric names, global scope, created on first use
- **Sparse arrays** — `array_set` / `array_get` with integer indices
- **Control flow** — `if` and `while` with multi-command bodies (tokens consumed by arity)
- **I/O** — `print` and `input`; invalid input becomes `0`
- **Clear errors** — division or modulo by zero raise with a helpful message
- **REPL + GUI** — interactive REPL and a simple Tkinter IDE (`nova_gui.py`)

## How to run

- **From a file:** `python interpreter.py path/to/program.nova`
- **REPL (interactive):** `python interpreter.py` with no arguments → `>>>` prompt; variables and arrays persist. Type `exit` or `quit` to quit.
- **GUI:** `python nova_gui.py` – editor, output pane, Run / Clear / New / Open / Save. (Requires Tkinter; on some Linux: `python3-tk`.)
- **From stdin:** `python interpreter.py < program.nova`
- **As a module:** `from interpreter import interpret; interpret("set x 1\nprint x")` → `"1"`

Requires **Python 3.7+**. No installation or dependencies.

## Documentation and examples

| Link | Description |
|------|-------------|
| [Language specification](docs/spec.md) | Full syntax, all commands, semantics, edge cases |
| [Tutorial](docs/tutorial.md) | Step-by-step intro with examples |
| [examples/](examples/) | Sample `.nova` programs (hello, factorial, array_demo, more) |

## Project layout

```
NovaLang/
├── interpreter.py    # Interpreter: interpret(program) -> output; REPL when run with no args
├── nova.py           # Runner: python nova.py [file.nova | gui] or python nova.py for REPL
├── nova_gui.py       # Tkinter GUI: editor + output + Run/Open/Save/Examples/Dark
├── smoke_test.py     # Quick smoke tests (run: python smoke_test.py)
├── docs/
│   ├── spec.md       # Language spec
│   └── tutorial.md   # Tutorial
├── examples/         # Example .nova programs
├── tests/            # Unit tests (unittest)
├── .github/workflows/tests.yml   # CI (tests on push/PR)
├── CONTRIBUTING.md   # How to contribute
├── CHANGELOG.md      # Release history
├── LICENSE           # MIT
└── README.md
```

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines (issues, PRs, and keeping the language minimal). Open an issue or PR on GitHub.

## License

MIT © 2025 Brandon Shoemaker — see [LICENSE](LICENSE).
