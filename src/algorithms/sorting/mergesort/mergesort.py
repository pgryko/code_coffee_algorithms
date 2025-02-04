from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array using the merge sort algorithm.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Args:
        arr: List of integers to be sorted

    Returns:
        Sorted list of integers
    """
    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide array into two halves
    mid = len(arr) // 2

    # Recursively sort the two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left: First sorted array
        right: Second sorted array

    Returns:
        Merged sorted array
    """
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements from both arrays and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add remaining elements from left array, if any
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Add remaining elements from right array, if any
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Example usage:
if __name__ == "__main__":
    # Test the merge sort implementation
    test_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = merge_sort(test_array)
    print(f"Original array: {test_array}")
    print(f"Sorted array: {sorted_array}")
