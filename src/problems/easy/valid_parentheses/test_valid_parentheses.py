import unittest

from valid_parentheses import isValid


class TestValidParentheses(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(isValid("()"))
        self.assertTrue(isValid("(())"))
        self.assertTrue(isValid("[()]"))
        self.assertTrue(isValid("()[]{}"))
        self.assertTrue(isValid("(1swe)"))
        self.assertTrue(isValid("(2)3[4]1{2}2"))

    def test_not_valid(self):
        self.assertFalse(isValid("("))
        self.assertFalse(isValid("(]"))
        self.assertFalse(isValid("([)]{}"))
        self.assertFalse(isValid("(1swe]"))
        self.assertFalse(isValid("(2[)34]1{2}2"))
