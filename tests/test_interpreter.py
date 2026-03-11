"""
Unit tests for the NovaLang interpreter.
"""

import unittest
import sys
from pathlib import Path

# Allow importing interpreter from project root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from interpreter import interpret


class TestBasicOps(unittest.TestCase):
    """Test set, add, sub, mul, div, mod, print."""

    def test_set_and_print(self):
        out = interpret("set x 42\nprint x")
        self.assertEqual(out, "42")

    def test_add_sub(self):
        out = interpret("set a 10\nadd a 5\nprint a\nsub a 3\nprint a")
        self.assertEqual(out, "15\n12")

    def test_mul_div_mod(self):
        out = interpret(
            "set n 7\nmul n 3\nprint n\n"
            "div n 7\nprint n\n"
            "mod n 2\nprint n"
        )
        self.assertEqual(out, "21\n3\n1")


class TestDefaults(unittest.TestCase):
    """Test undefined variable defaults: 0 for most, 1 for mul."""

    def test_undefined_defaults_to_zero(self):
        out = interpret("add x 10\nprint x")
        self.assertEqual(out, "10")

    def test_mul_undefined_defaults_to_one(self):
        out = interpret("mul y 5\nprint y")
        self.assertEqual(out, "5")


class TestControlFlow(unittest.TestCase):
    """Test if and while."""

    def test_if_true(self):
        out = interpret("set n 5\nif n eq 5 set ok 1\nprint ok")
        self.assertEqual(out, "1")

    def test_if_false(self):
        out = interpret("set n 3\nif n eq 5 set ok 1\nprint ok")
        self.assertEqual(out, "0")

    def test_while_decrement(self):
        out = interpret("set n 3\nwhile n gt 0 sub n 1\nprint n")
        self.assertEqual(out, "0")

    def test_while_multi_command_body_factorial(self):
        # Multi-command while body: mul fact n sub n 1 per iteration
        program = "set n 5\nset fact 1\nwhile n gt 0 mul fact n sub n 1\nprint fact"
        out = interpret(program)
        self.assertEqual(out, "120")


class TestArrays(unittest.TestCase):
    """Test array_set and array_get (sparse)."""

    def test_array_set_get(self):
        out = interpret(
            "array_set a 0 10\narray_set a 1 20\n"
            "array_get x a 0\narray_get y a 1\n"
            "print x\nprint y"
        )
        self.assertEqual(out, "10\n20")

    def test_array_missing_index_defaults_to_zero(self):
        out = interpret("array_set a 0 7\narray_get z a 99\nprint z")
        self.assertEqual(out, "0")


class TestErrors(unittest.TestCase):
    """Test division/modulo by zero and malformed input."""

    def test_div_by_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            interpret("set x 1\ndiv x 0")
        self.assertIn("division by zero", str(ctx.exception))

    def test_mod_by_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            interpret("set x 1\nmod x 0")
        self.assertIn("modulo by zero", str(ctx.exception))

    def test_unknown_command_raises(self):
        with self.assertRaises(ValueError) as ctx:
            interpret("foo bar")
        self.assertIn("Unknown command", str(ctx.exception))


class TestInput(unittest.TestCase):
    """Test input command with mocked stdin."""

    def test_input_stores_value(self):
        def fake_input():
            return "99"
        out = interpret("input x\nprint x", input_fn=fake_input)
        self.assertEqual(out, "99")

    def test_input_invalid_defaults_to_zero(self):
        def fake_input():
            return "not a number"
        out = interpret("input x\nprint x", input_fn=fake_input)
        self.assertEqual(out, "0")


if __name__ == "__main__":
    unittest.main()
