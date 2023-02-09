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
