import unittest

from array_string_questions import (
    isoneaway,
    ispalindromepermutation,
    ispermutation,
    isunique,
    stringcompress,
)


class TestIsUnique(unittest.TestCase):
    def test_isunique(self):
        # Test Empty string
        self.assertTrue(isunique(""))
        self.assertTrue(isunique("AB34"))
        self.assertFalse(isunique("AB34A"))
        self.assertFalse(isunique("AAB34"))


class TestIsPermutation(unittest.TestCase):
    def test_ispermutation(self):
        # Test Empty string
        self.assertTrue(ispermutation("", ""))
        self.assertTrue(ispermutation("AB34", "4AB3"))
        self.assertTrue(ispermutation("AB34A", "AB34A"))
        self.assertFalse(ispermutation("AB33A", "AB34A"))
        self.assertFalse(ispermutation("AB34A", "AB34"))


class TestIsPalindromePermutation(unittest.TestCase):
    def test_ispalindromepermutation(self):
        self.assertFalse(ispalindromepermutation(""))
        self.assertTrue(ispalindromepermutation("ABBA"))
        self.assertFalse(ispalindromepermutation("ABBC"))
        self.assertTrue(ispalindromepermutation("ABCBA"))
        self.assertTrue(ispalindromepermutation("ABCCA"))
        self.assertFalse(ispalindromepermutation("AKCAI"))


class TestIsOneAway(unittest.TestCase):
    def test_isoneaway(self):
        # Test Empty string
        self.assertFalse(isoneaway("", ""))
        self.assertFalse(isoneaway("ABC", "ABC"))
        # Test Deletion
        self.assertTrue(isoneaway("ABC", "BC"))
        self.assertTrue(isoneaway("ABC", "AC"))
        self.assertTrue(isoneaway("ABC", "AB"))
        # # Test Replacement
        self.assertTrue(isoneaway("ABC", "DBC"))
        self.assertTrue(isoneaway("ABC", "ADC"))
        self.assertTrue(isoneaway("ABC", "ABD"))
        # # Test Insert
        self.assertTrue(isoneaway("ABC", "DABC"))
        self.assertTrue(isoneaway("ABC", "ADBC"))
        self.assertTrue(isoneaway("ABC", "ABDC"))
        self.assertTrue(isoneaway("ABC", "ABCD"))


class TestStringCompress(unittest.TestCase):
    def test_stringcompress(self):
        self.assertEqual(stringcompress("aabccccaaa"), "a2b1c4a3")
