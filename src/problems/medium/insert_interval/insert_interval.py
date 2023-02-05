from typing import List

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by
starti. You are also given an interval newInterval = [start, end] that represents the start and
end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by
starti and intervals still does not have any overlapping intervals (merge overlapping intervals
if necessary).

Return intervals after the insertion.


Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""
from collections import deque


def overlap(interval1: tuple, interval2: tuple):
    def _overlap(interval_1: tuple, interval_2: tuple):
        if interval_1[0] <= interval_2[0] <= interval_1[1]:
            return True

        if interval_1[0] <= interval_2[1] <= interval_1[1]:
            return True

        return False

    return _overlap(interval1, interval2) or _overlap(interval2, interval1)


def merge_interval(interval: tuple, new_interval: tuple):
    return min(interval[0], new_interval[0]), max(interval[1], new_interval[1])


def insert_interval(intervals: List[tuple], new_interval: tuple) -> List[tuple]:
    new_stack = deque()

    if new_interval[0] <= intervals[0][0]:
        new_stack.append(new_interval)
        new_interval = None

    for i in range(0, len(intervals)):
        tmp_tuple = intervals[i]

        if new_interval and overlap(tmp_tuple, new_interval):
            tmp_tuple = merge_interval(tmp_tuple, new_interval)

        if i < len(intervals) - 1 and overlap(intervals[i], intervals[i + 1]):
            tmp_tuple = merge_interval(intervals[i], intervals[i + 1])

        if len(new_stack) > 0 and overlap(new_stack[-1], tmp_tuple):
            new_stack[-1] = merge_interval(new_stack[-1], tmp_tuple)
        else:
            new_stack.append(tmp_tuple)

        if (
            new_interval
            and i < len(intervals) - 1
            and tmp_tuple[1] < new_interval[0] < intervals[i + 1][0]
        ):
            new_stack.append(new_interval)
            new_interval = None

    # Handle case where we have not already inserted the interval
    if new_interval:
        if len(new_stack) > 0 and overlap(new_stack[-1], new_interval):
            new_stack[-1] = merge_interval(new_stack[-1], new_interval)
        else:
            new_stack.append(new_interval)

    return list(new_stack)
