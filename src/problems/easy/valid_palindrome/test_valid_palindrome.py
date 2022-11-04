import unittest

from valid_palindrome import is_valid_palindrome


class TestValidPalindrome(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(is_valid_palindrome("A man, a plan, a canal: Panama"), True)

    def test_invalid(self):
        self.assertEqual(is_valid_palindrome("race a car"), False)

    def test_empty_space(self):
        self.assertEqual(is_valid_palindrome(" "), True)
