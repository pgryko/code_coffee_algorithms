from typing import List


def search_iterative(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:

        # The //2 is a integer division by python
        # so 5//2 -> 2
        mid = (high + low) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            low = mid + 1

        if nums[mid] > target:
            high = mid - 1

    # If nothing is found python will by default return None


def search_recursive(nums: List[int], target: int) -> int:
    def _recursive(nums: List[int], target: int, low, high):
        if low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                return _recursive(nums, target, low=mid + 1, high=high)

            if nums[mid] > target:
                return _recursive(nums, target, low=low, high=mid - 1)

    return _recursive(nums=nums, target=target, low=0, high=len(nums) - 1)
