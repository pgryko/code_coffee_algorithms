from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:

    hashmap = {}

    for i in range(0, len(nums)):

        needed_complement = target - nums[i]

        if needed_complement in hashmap:
            return [hashmap[needed_complement], i]

        hashmap[nums[i]] = i
