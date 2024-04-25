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


def overlap(interval1: tuple, interval2: tuple):

    return interval1[0] <= interval2[1] and interval1[1] >= interval2[0]


def merge_interval(interval: tuple, new_interval: tuple):
    return min(interval[0], new_interval[0]), max(interval[1], new_interval[1])


def insert_interval(intervals: List[tuple], new_interval: tuple) -> List[tuple]:

    if len(intervals) == 0:
        return [new_interval]

    if new_interval[1] <= intervals[0][0]:
        return [new_interval] + intervals

    new_stack = []

    current_interval = new_interval

    for i in range(len(intervals)):

        if overlap(current_interval, intervals[i]):
            current_interval = merge_interval(current_interval, intervals[i])

        elif current_interval[1] < intervals[i][0]:
            new_stack.append(current_interval)
            new_stack += intervals[i:]

            return new_stack

        else:
            new_stack += [intervals[i]]

    new_stack.append(current_interval)

    return new_stack
