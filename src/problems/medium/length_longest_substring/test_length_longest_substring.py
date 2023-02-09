import unittest

from src.problems.medium.length_longest_substring.length_longest_substring import (
    longest_substring,
)


class TestLongestSubstring(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(longest_substring("abcabcbb"), 3)

    def test_simple_string_2(self):
        self.assertEqual(longest_substring("dvdf"), 3)

    def test_simple_string_3(self):
        self.assertEqual(longest_substring("dvvdf"), 3)

    def test_same_string(self):
        self.assertEqual(longest_substring("aaaaa"), 1)

    def test_explicit_substring(self):
        self.assertEqual(longest_substring("pwwkew"), 3)

    def test_single_char(self):
        self.assertEqual(longest_substring("a"), 1)

    def test_empty_char(self):
        self.assertEqual(longest_substring(" "), 1)

    def test_no_char(self):
        self.assertEqual(longest_substring(""), 0)

    def test_two_chars(self):
        self.assertEqual(longest_substring("au"), 2)
