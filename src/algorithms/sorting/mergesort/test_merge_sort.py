import unittest

from src.algorithms.sorting.mergesort.mergesort import merge_sort, merge


class TestMergeFunction:
    """Test suite for the merge function of the merge sort algorithm."""

    def test_merge_empty_lists(self):
        """Test merging two empty lists."""
        assert merge([], []) == []

    def test_merge_one_empty_list(self):
        """Test merging when one list is empty."""
        # Test empty left list
        assert merge([], [1, 2, 3]) == [1, 2, 3]
        # Test empty right list
        assert merge([1, 2, 3], []) == [1, 2, 3]

    def test_merge_equal_length_lists(self):
        """Test merging lists of equal length."""
        left = [1, 3, 5]
        right = [2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        assert merge(left, right) == expected

    def test_merge_different_length_lists(self):
        """Test merging lists of different lengths."""
        # Left list longer
        assert merge([1, 3, 5, 7], [2, 4]) == [1, 2, 3, 4, 5, 7]
        # Right list longer
        assert merge([1, 3], [2, 4, 6, 8]) == [1, 2, 3, 4, 6, 8]

    def test_merge_with_duplicates(self):
        """Test merging lists containing duplicate values."""
        left = [1, 2, 2, 3]
        right = [2, 3, 4, 4]
        expected = [1, 2, 2, 2, 3, 3, 4, 4]
        assert merge(left, right) == expected

    def test_merge_negative_numbers(self):
        """Test merging lists with negative numbers."""
        left = [-5, -3, 1]
        right = [-4, -2, 0]
        expected = [-5, -4, -3, -2, 0, 1]
        assert merge(left, right) == expected

    def test_merge_single_element_lists(self):
        """Test merging lists with single elements."""
        assert merge([1], [2]) == [1, 2]
        assert merge([2], [1]) == [1, 2]

    def test_merge_already_sorted_lists(self):
        """Test merging lists that are already in sorted order."""
        left = [1, 2, 3]
        right = [4, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]
        assert merge(left, right) == expected

    def test_merge_input_unchanged(self):
        """Test that the input lists are not modified by the merge operation."""
        left = [1, 3, 5]
        right = [2, 4, 6]
        left_copy = left.copy()
        right_copy = right.copy()

        merge(left, right)

        assert left == left_copy
        assert right == right_copy


class Testmerge_sort(unittest.TestCase):
    def test_sort_basic(self):
        array_in = [5, 4, 2, 1, 6, 3, 1]
        self.assertEqual(merge_sort(array_in), [1, 1, 2, 3, 4, 5, 6])

    def test_sort_basic_even(self):
        array_in = [5, 4, 2, 1, 6, 1]
        self.assertEqual(merge_sort(array_in), [1, 1, 2, 4, 5, 6])

    def test_sort_zero(self):
        array_in = [5, 4, 2, 0, 1, 6, 3, 1]
        self.assertEqual(merge_sort(array_in), [0, 1, 1, 2, 3, 4, 5, 6])

    def test_sort_negative(self):
        array_in = [5, 4, 2, 1, -6, 3, 1]
        self.assertEqual(merge_sort(array_in), [-6, 1, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
