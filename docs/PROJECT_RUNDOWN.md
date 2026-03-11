# NovaLang Project Rundown

**Last updated:** March 2025 (v0.1 – initial public release)

## What is NovaLang?

NovaLang is a **minimal, intentionally simple, imperative programming language** focused exclusively on **integer arithmetic**, designed to be:

- extremely easy to read and write for beginners
- **forgiving** by default (prevents most "undefined variable" crashes)
- useful as a teaching tool and quick math prototyping environment

It is **not** trying to compete with Python, JavaScript, Rust, or Go.  
It is deliberately limited to keep the mental model tiny and the learning curve almost flat.

### Core Philosophy

1. One command per line. No indentation, no semicolons, no parentheses hell.
2. Variables appear when you use them — no declarations required.
3. Undefined variables default to sensible values:
   - `0` for `add`, `sub`, `div`, `mod`, `set` (when referencing), `print`, `array_get`
   - `1` for `mul` (so multiplying an undefined variable doesn't silently zero everything)
4. Only integers. No strings, floats, booleans, objects, classes — nothing else.
5. Goal = maximum signal-to-noise for learning imperative basics and doing small arithmetic scripts.

## Current Feature Set (v0.1)

- **Commands**:
  - `set var value`
  - `add var value` / `sub var value` / `mul var value` / `div var value` / `mod var value`
  - `print var`
  - `input var` (reads integer from stdin, defaults to 0 on bad input)
  - `if var op value cmd ...` (op = eq gt lt geq leq) — body is one or more commands (space-separated, consumed by arity)
  - `while var op value cmd ...` — same; body runs each iteration until condition is false
  - `array_set var index value` / `array_get dest src index` (sparse integer arrays via dict backend)

- **Execution model**: strictly sequential, global scope, top-to-bottom
- **Error handling**: only divide/modulo by zero raises; everything else uses defaults
- **Implementation**: single-file Python 3 interpreter (`interpreter.py`)

## Example Programs (real output verified)

**Hello-style (set + print)**

```nova
set x 42
print x
```

Output: `42`

**Factorial of 5**

The `while` body can list multiple commands; they are run in order each iteration (tokens consumed by command arity):

```nova
set n 5
set fact 1
while n gt 0 mul fact n sub n 1
print fact
```

Output: `120`

**Count down with while**

```nova
set n 3
while n gt 0 sub n 1
print n
```

Output: `0`

**Array and sum**

```nova
array_set a 0 10
array_set a 1 20
array_get x a 0
array_get y a 1
set total 0
add total x
add total y
print total
```

Output: `30`

See [spec.md](spec.md) for full syntax and [examples/](../examples/) for more programs.
