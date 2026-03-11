# NovaLang Tutorial (v0.1)

A step-by-step intro to NovaLang with small examples.

## 1. Running a program

Run a `.nova` file:

```bash
python interpreter.py program.nova
```

Or use the interpreter from Python:

```python
from interpreter import interpret
out = interpret("set x 1\nprint x")
print(out)  # "1"
```

## 2. Variables and arithmetic

Variables are created on first use. Use `set` to assign, then `add`, `sub`, `mul`, `div`, and `mod` to update.

**Example: Basic arithmetic**

```
set a 10
set b 3
add a b
print a
sub a 2
print a
```

- `set a 10` and `set b 3` set `a` and `b`.
- `add a b` → `a = 10 + 3 = 13`. First output: `13`.
- `sub a 2` → `a = 11`. Second output: `11`.

**Example: Multiplication default**

If you use `mul` on an undefined variable, it is treated as 1:

```
mul x 5
print x
```

Output: `5` (undefined `x` → 1, then 1*5=5).

## 3. Conditionals

**if** runs one command when a condition is true: `if var op value cmd ...args`.

**Example: if**

```
set score 42
if score geq 40 set pass 1
if pass eq 1 print score
```

Output: `42`.

## 4. Loops

**while** runs one command repeatedly while the condition is true. The condition uses the same variable you typically update in the loop body so it eventually becomes false.

**Example: Count down**

```
set n 3
while n gt 0 sub n 1
print n
```

After the loop, `n` is 0. Output: `0`.

**Example: Sum 1..5 (unrolled)**

Because each `while` runs only one command per iteration, we can't both add and decrement in one loop. For a fixed range we can unroll.

```
set sum 0
add sum 5
add sum 4
add sum 3
add sum 2
add sum 1
print sum
```

Output: `15`.

## 5. Arrays

Arrays are sparse: only set indices exist. Use `array_set` to write and `array_get` to read (missing index → 0).

**Example: Array read/write**

```
array_set a 0 10
array_set a 1 20
array_get x a 0
array_get y a 1
print x
print y
```

Output: `10` then `20`.

**Example: Sum of array elements (unrolled)**

```
array_set arr 0 3
array_set arr 1 7
array_set arr 2 2
array_get v0 arr 0
array_get v1 arr 1
array_get v2 arr 2
set total 0
add total v0
add total v1
add total v2
print total
```

Output: `12`.

For more detail and edge cases, see the [language specification](spec.md).
