from typing import List


def in_interval(interval, new_interval):

    if interval[0] <= new_interval[0] <= interval[1]:
        return True

    return interval[0] <= new_interval[1] <= interval[1]


def insert_interval(
    intervals: List[List[int]], newInterval: List[int]
) -> List[List[int]]:

    for i in range(0, len(intervals)):
        # Case 1

        if in_interval(intervals[i], newInterval):
            intervals[i][0] = min(intervals[i][0], newInterval[0])
            intervals[i][1] = max(intervals[i][1], newInterval[1])

    return intervals
