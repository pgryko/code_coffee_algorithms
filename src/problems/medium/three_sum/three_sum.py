"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
from typing import List


def _sum_append(sorted_list, three_sum_list, first_ptr, end_ptr):
    sum_list = [
        sorted_list[first_ptr] + sorted_list[first_ptr + 1] + sorted_list[end_ptr]
    ]

    if sum(sum_list) == 0:
        three_sum_list.append(sum_list)

    sum_list = [
        sorted_list[-first_ptr] + sorted_list[-first_ptr - 1] + sorted_list[-end_ptr]
    ]

    if sum(sum_list) == 0:
        three_sum_list.append(sum_list)

    return three_sum_list


def three_sum(nums: List[int]) -> List[List[int]]:
    sorted_list = sorted([-1, 0, 1, 2, -1, -4])

    # Let first ptr cover two elements
    first_ptr = 0
    end_ptr = len(nums) - 1

    three_sum_list = []

    while (
        0 <= first_ptr < len(nums) - 1
        and 0 <= end_ptr < len(nums)
        and first_ptr != end_ptr
    ):

        sum_list = [
            sorted_list[first_ptr] + sorted_list[first_ptr + 1] + sorted_list[end_ptr]
        ]

        if sum(sum_list) == 0:
            three_sum_list.append(sum_list)

        sum_list = [
            sorted_list[-first_ptr]
            + sorted_list[-first_ptr - 1]
            + sorted_list[-end_ptr]
        ]

        if sum(sum_list) == 0:
            three_sum_list.append(sum_list)

        first_ptr += 1

    return three_sum_list
