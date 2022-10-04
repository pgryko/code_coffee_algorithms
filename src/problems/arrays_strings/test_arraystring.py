import unittest

from array_string_questions import (
    is_oneaway,
    is_palindrome_permutation,
    is_permutation,
    is_unique,
    string_compress,
    rotate_matrix,
    reflect_matrix,
    transpose_matrix,
)


class TestIsUnique(unittest.TestCase):
    def test_is_unique(self):
        # Test Empty string
        self.assertTrue(is_unique(""))
        self.assertTrue(is_unique("AB34"))
        self.assertFalse(is_unique("AB34A"))
        self.assertFalse(is_unique("AAB34"))


class TestIsPermutation(unittest.TestCase):
    def test_is_permutation(self):
        # Test Empty string
        self.assertTrue(is_permutation("", ""))
        self.assertTrue(is_permutation("AB34", "4AB3"))
        self.assertTrue(is_permutation("AB34A", "AB34A"))
        self.assertFalse(is_permutation("AB33A", "AB34A"))
        self.assertFalse(is_permutation("AB34A", "AB34"))


class TestIsPalindromePermutation(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        self.assertFalse(is_palindrome_permutation(""))
        self.assertTrue(is_palindrome_permutation("ABBA"))
        self.assertFalse(is_palindrome_permutation("ABBC"))
        self.assertTrue(is_palindrome_permutation("ABCBA"))
        self.assertTrue(is_palindrome_permutation("ABCCA"))
        self.assertFalse(is_palindrome_permutation("AKCAI"))


class TestIsOneAway(unittest.TestCase):
    def test_is_one_away(self):
        # Test Empty string
        self.assertFalse(is_oneaway("", ""))
        self.assertFalse(is_oneaway("ABC", "ABC"))
        # Test Deletion
        self.assertTrue(is_oneaway("ABC", "BC"))
        self.assertTrue(is_oneaway("ABC", "AC"))
        self.assertTrue(is_oneaway("ABC", "AB"))
        # # Test Replacement
        self.assertTrue(is_oneaway("ABC", "DBC"))
        self.assertTrue(is_oneaway("ABC", "ADC"))
        self.assertTrue(is_oneaway("ABC", "ABD"))
        # # Test Insert
        self.assertTrue(is_oneaway("ABC", "DABC"))
        self.assertTrue(is_oneaway("ABC", "ADBC"))
        self.assertTrue(is_oneaway("ABC", "ABDC"))
        self.assertTrue(is_oneaway("ABC", "ABCD"))


class TestStringCompress(unittest.TestCase):
    def test_string_compress(self):
        self.assertEqual(string_compress("aabccccaaa"), "a2b1c4a3")


class TestRotateMatrix(unittest.TestCase):
    def test_reflect_matrix_odd(self):
        self.assertEqual(
            reflect_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[7, 8, 9], [4, 5, 6], [1, 2, 3]],
        )

    def test_reflect_matrix_even(self):
        self.assertEqual(
            reflect_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [8, 2, 3]]),
            [[8, 2, 3], [7, 8, 9], [4, 5, 6], [1, 2, 3]],
        )

    def test_transpose_matrix_symmetric(self):
        self.assertEqual(
            transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        )

    def test_rotate_matrix_1(self):
        self.assertEqual(
            rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        )

    def test_rotate_matrix_2(self):
        self.assertEqual(
            rotate_matrix(
                [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
            ),
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        )
