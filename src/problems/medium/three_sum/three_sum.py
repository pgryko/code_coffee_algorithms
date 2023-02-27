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


def three_sum(nums: List[int]) -> List[List[int]]:
    """Given an integer array nums, return all unique triplets

    Args:
        nums: Integer array

    Returns: Unique triplets

    a + b + c = 0

    reduces the problem to two sum

    -c = a + b

    """

    sorted_list = sorted(nums)
    three_sum_list = []

    for i in range(0, len(sorted_list) - 1):
        j = i + 1
        r = len(sorted_list) - 1

        while j < r:
            if sorted_list[i] + sorted_list[j] + sorted_list[r] == 0:
                if len(three_sum_list) == 0 or three_sum_list[-1] != [
                    sorted_list[i],
                    sorted_list[j],
                    sorted_list[r],
                ]:
                    three_sum_list.append(
                        [sorted_list[i], sorted_list[j], sorted_list[r]]
                    )
                j = j + 1
            elif sorted_list[i] + sorted_list[j] + sorted_list[r] < 0:
                j = j + 1
            else:
                r = r - 1

    return three_sum_list
