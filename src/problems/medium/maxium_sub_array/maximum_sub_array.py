"""
Given an integer array nums, find the
subarray which has the largest sum and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Linear solution involves using a sliding window

"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    current_max = nums[0]

    max_current_window = 0

    for i in range(0, len(nums)):
        max_current_window += nums[i]

        if max_current_window > current_max:
            current_max = max_current_window

        if max_current_window < 0:
            max_current_window = 0

    return current_max
