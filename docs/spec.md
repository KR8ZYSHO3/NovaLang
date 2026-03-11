# NovaLang Language Specification (v0.1.1)

## Overview

NovaLang is a minimal, line-based, imperative language for integer arithmetic. It has a single global scope, dynamic variables, and forgiving defaults for undefined names.

## Syntax

- **Lines:** One command per line; commands are space-separated tokens.
- **Whitespace:** Empty lines and leading/trailing spaces are ignored. Lines whose first non-space character is `#` are treated as comments and ignored.
- **Case:** Command names are case-insensitive (e.g. `SET`, `set`, `Set` are equivalent).
- **Values:** Integer literals (e.g. `0`, `42`, `-7`) or variable names (alphanumeric).

## Types

- **v0.1:** Only integers. No floats, strings, or booleans.

## Variables

- Names are alphanumeric (e.g. `x`, `n`, `count2`).
- Variables are created on first use; there are no declarations.
- **Scope:** Global only.
- **Defaults when undefined:**
  - **0** for: set (RHS), add, sub, div, mod, print, condition operands, array index/value.
  - **1** for: multiplication (so `mul x 5` when `x` is undefined does `1 * 5` → `x = 5`).

## Commands

### Assignment and arithmetic

| Command | Form | Description |
|--------|------|-------------|
| `set` | `set var value` | Assign `value` (literal or variable) to `var`. |
| `add` | `add var value` | `var = var + value` (undefined `var` → 0). |
| `sub` | `sub var value` | `var = var - value`. |
| `mul` | `mul var value` | `var = var * value` (undefined `var` → 1). |
| `div` | `div var value` | `var = var // value` (integer division). **Errors** if `value` is 0. |
| `mod` | `mod var value` | `var = var % value`. **Errors** if `value` is 0. |

Examples:

```
set x 10
add x 5
print x
```
Output: `15`

```
mul y 3
print y
```
Output: `3` (y was undefined → 1, then 1*3=3).

### I/O

| Command | Form | Description |
|--------|------|-------------|
| `print` | `print var` | Output the value of `var` (as integer string). |
| `input` | `input var` | Read one line from stdin, parse as integer, store in `var`. Invalid or EOF → `0`. |

### Control flow

| Command | Form | Description |
|--------|------|-------------|
| `if` | `if var op value cmd ...args` | If condition is true, execute the body (one or more commands) once. |
| `while` | `while var op value cmd ...args` | While condition is true, repeatedly execute the body (one or more commands). |

**Operators:** `eq` (==), `gt` (>), `lt` (<), `geq` (>=), `leq` (<=).

**Body:** The rest of the line after `value` is a sequence of commands. Tokens are consumed by each command’s arity (e.g. `set`/`add`/`mul` take 3 tokens, `print`/`input` take 2, `array_set` 4, `array_get` 4). So `while n gt 0 mul fact n sub n 1` runs `mul fact n` then `sub n 1` each iteration.

Examples:

```
set x 5
if x eq 5 set y 1
print y
```
Output: `1`

```
set n 5
set fact 1
while n gt 0 mul fact n sub n 1
print fact
```
Output: `120` (5!). The body has two commands per iteration: `mul fact n` then `sub n 1`.

### Arrays

Arrays are sparse (only set indices exist). Internally they behave like maps from integer index to integer value.

| Command | Form | Description |
|--------|------|-------------|
| `array_set` | `array_set var index value` | Set `var[index] = value`. `var` is the array name; index and value can be literal or variable. |
| `array_get` | `array_get dest src index` | `dest = src[index]`; if index not set, `0`. |

Examples:

```
array_set a 0 10
array_set a 1 20
array_get x a 0
array_get y a 1
print x
print y
```
Output: `10` then `20`.

```
array_get z a 99
print z
```
Output: `0` (missing index).

## Execution model

- Execution is **sequential**, top to bottom.
- Each line is either empty (skip) or one command.
- `if` runs its sub-command at most once when the condition holds.
- `while` re-evaluates the condition each time; when true it runs the sub-command and then repeats from the same `while` line (no block scope).

## Edge cases and errors

- **Division by zero:** `div var 0` or `div var x` when `x` is 0 → **Error** (e.g. `ValueError`).
- **Modulo by zero:** `mod var 0` → **Error**.
- **Invalid input:** `input var` on non-integer or EOF → store `0` in `var`.
- **Malformed lines:** Unknown command or wrong number of arguments → **Error** with a clear message (e.g. line number + message).
- **Missing array index:** `array_get dest arr index` when `index` was never set in `arr` → `0`.

## Summary of defaults

| Context | Undefined variable value |
|--------|---------------------------|
| RHS of set, add, sub, div, mod; print; condition; array index/value | 0 |
| LHS of mul (current value of var) | 1 |
| array_get missing index | 0 |
