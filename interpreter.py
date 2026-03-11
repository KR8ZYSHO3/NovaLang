"""
NovaLang Interpreter v0.1.1

A minimal, line-based interpreter for integer arithmetic. Variables and arrays
live in global scope; undefined variables default to 0 (or 1 for multiplication).
Entrypoint: interpret(program: str, input_fn=None, variables=None, arrays=None) -> str (all print output).
Optional variables/arrays allow REPL to persist state across lines.
"""

from typing import Dict, List, Optional

# Number of tokens per command (command name + args). Used to chunk if/while bodies.
_CMD_ARITY = {
    "set": 3, "add": 3, "sub": 3, "mul": 3, "div": 3, "mod": 3,
    "print": 2, "input": 2,
    "array_set": 4, "array_get": 4,
}


def _parse_int(s: str) -> Optional[int]:
    """Parse string as integer; return None if invalid."""
    s = s.strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def _get_value(
    token: str,
    variables: Dict[str, int],
    default: int = 0,
) -> int:
    """
    Resolve a token to an integer: literal or variable lookup.
    Undefined variables return `default` (0 for most ops, 1 for mul).
    """
    val = _parse_int(token)
    if val is not None:
        return val
    return variables.get(token, default)


def _eval_condition(
    var_name: str,
    op: str,
    value_token: str,
    variables: Dict[str, int],
) -> bool:
    """Evaluate a condition: var op value. Uses 0 for undefined var."""
    left = _get_value(var_name, variables, default=0)
    right = _get_value(value_token, variables, default=0)
    if op == "eq":
        return left == right
    if op == "gt":
        return left > right
    if op == "lt":
        return left < right
    if op == "geq":
        return left >= right
    if op == "leq":
        return left <= right
    raise ValueError(f"Unknown comparison operator: {op}")


def _run_line(
    line: str,
    variables: Dict[str, int],
    arrays: Dict[str, Dict[int, int]],
    output_lines: List[str],
    input_fn,
) -> None:
    """
    Execute a single line of NovaLang. Modifies variables, arrays, and output_lines.
    """
    line = line.strip()
    if not line:
        return
    parts = line.split()
    if not parts:
        return

    cmd = parts[0].lower()

    if cmd == "set":
        if len(parts) < 3:
            raise ValueError("set requires: set var value")
        var, value_token = parts[1], parts[2]
        variables[var] = _get_value(value_token, variables)

    elif cmd == "add":
        if len(parts) < 3:
            raise ValueError("add requires: add var value")
        var, value_token = parts[1], parts[2]
        current = variables.get(var, 0)
        variables[var] = current + _get_value(value_token, variables)

    elif cmd == "sub":
        if len(parts) < 3:
            raise ValueError("sub requires: sub var value")
        var, value_token = parts[1], parts[2]
        current = variables.get(var, 0)
        variables[var] = current - _get_value(value_token, variables)

    elif cmd == "mul":
        if len(parts) < 3:
            raise ValueError("mul requires: mul var value")
        var, value_token = parts[1], parts[2]
        current = variables.get(var, 1)  # default 1 for multiplication
        variables[var] = current * _get_value(value_token, variables)

    elif cmd == "div":
        if len(parts) < 3:
            raise ValueError("div requires: div var value")
        var, value_token = parts[1], parts[2]
        divisor = _get_value(value_token, variables)
        if divisor == 0:
            raise ValueError("division by zero")
        current = variables.get(var, 0)
        variables[var] = current // divisor

    elif cmd == "mod":
        if len(parts) < 3:
            raise ValueError("mod requires: mod var value")
        var, value_token = parts[1], parts[2]
        divisor = _get_value(value_token, variables)
        if divisor == 0:
            raise ValueError("modulo by zero")
        current = variables.get(var, 0)
        variables[var] = current % divisor

    elif cmd == "print":
        if len(parts) < 2:
            raise ValueError("print requires: print var")
        var = parts[1]
        output_lines.append(str(variables.get(var, 0)))

    elif cmd == "input":
        if len(parts) < 2:
            raise ValueError("input requires: input var")
        var = parts[1]
        try:
            variables[var] = int(input_fn().strip())
        except (ValueError, EOFError):
            variables[var] = 0

    elif cmd == "array_set":
        if len(parts) < 4:
            raise ValueError("array_set requires: array_set var index value")
        var, index_token, value_token = parts[1], parts[2], parts[3]
        if var not in arrays:
            arrays[var] = {}
        idx = _get_value(index_token, variables)
        val = _get_value(value_token, variables)
        arrays[var][idx] = val

    elif cmd == "array_get":
        if len(parts) < 4:
            raise ValueError("array_get requires: array_get dest src index")
        dest, src, index_token = parts[1], parts[2], parts[3]
        arr = arrays.get(src, {})
        idx = _get_value(index_token, variables)
        variables[dest] = arr.get(idx, 0)

    else:
        raise ValueError(f"Unknown command: {cmd}")


def _run_body_tokens(
    tokens: List[str],
    variables: Dict[str, int],
    arrays: Dict[str, Dict[int, int]],
    output_lines: List[str],
    input_fn,
) -> None:
    """
    Run a sequence of commands from a token list (e.g. body of if/while).
    Tokens are consumed by command arity; each command is executed in order.
    """
    i = 0
    while i < len(tokens):
        cmd = tokens[i].lower()
        arity = _CMD_ARITY.get(cmd)
        if arity is None:
            raise ValueError(f"Unknown command in body: {cmd}")
        if i + arity > len(tokens):
            raise ValueError(f"Command {cmd} requires {arity} tokens, not enough in body")
        line = " ".join(tokens[i : i + arity])
        _run_line(line, variables, arrays, output_lines, input_fn)
        i += arity


def interpret(
    program: str,
    input_fn=None,
    variables: Optional[Dict[str, int]] = None,
    arrays: Optional[Dict[str, Dict[int, int]]] = None,
) -> str:
    """
    Run a NovaLang program and return all printed output as a single string
    (one line per print, joined by newlines).

    :param program: Full program source as a string.
    :param input_fn: Optional callable that returns a line of input (default: built-in input).
    :param variables: Optional dict to use and mutate (for REPL state). If None, a fresh dict is used.
    :param arrays: Optional dict to use and mutate (for REPL state). If None, a fresh dict is used.
    :return: Concatenated output lines from print statements.
    """
    if input_fn is None:
        input_fn = input
    if variables is None:
        variables = {}
    if arrays is None:
        arrays = {}
    output_lines: List[str] = []
    lines = program.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        parts = stripped.split()
        cmd = parts[0].lower()

        if cmd == "if":
            if len(parts) < 5:
                raise ValueError("if requires: if var op value cmd ...args")
            var_name, op, value_token = parts[1], parts[2], parts[3]
            body_tokens = parts[4:]
            if _eval_condition(var_name, op, value_token, variables):
                _run_body_tokens(body_tokens, variables, arrays, output_lines, input_fn)
            i += 1
            continue

        if cmd == "while":
            if len(parts) < 5:
                raise ValueError("while requires: while var op value cmd ...args")
            var_name, op, value_token = parts[1], parts[2], parts[3]
            body_tokens = parts[4:]
            if _eval_condition(var_name, op, value_token, variables):
                _run_body_tokens(body_tokens, variables, arrays, output_lines, input_fn)
                # Re-evaluate condition next iteration (do not advance line index)
            else:
                i += 1
            continue

        try:
            _run_line(stripped, variables, arrays, output_lines, input_fn)
        except ValueError as e:
            raise ValueError(f"Line {i + 1}: {e}") from e
        i += 1

    return "\n".join(output_lines)


def repl() -> None:
    """Interactive REPL: read lines, interpret with persistent variables/arrays, print output."""
    print("NovaLang REPL (v0.1.1) – type 'exit' or 'quit' or Ctrl+C/Ctrl+D to quit")
    print("Variables and arrays persist across lines.\n")
    variables: Dict[str, int] = {}
    arrays: Dict[str, Dict[int, int]] = {}
    while True:
        try:
            line = input(">>> ").strip()
            if not line:
                continue
            if line.lower() in ("exit", "quit", ":q"):
                print("Goodbye.")
                break
            result = interpret(line, input_fn=input, variables=variables, arrays=arrays)
            if result:
                print(result)
        except EOFError:
            print("\nGoodbye.")
            break
        except KeyboardInterrupt:
            print("\nGoodbye.")
            break
        except Exception as e:
            print(f"Error: {e}")


def main() -> None:
    """Entry point: run a .nova file, stdin, or REPL when no args and interactive."""
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            program = f.read()
        result = interpret(program)
        if result:
            print(result)
    elif sys.stdin.isatty():
        repl()
    else:
        program = sys.stdin.read()
        result = interpret(program)
        if result:
            print(result)


if __name__ == "__main__":
    main()
