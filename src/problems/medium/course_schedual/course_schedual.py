"""
Course Schedule
Medium
12.9K
511
Companies
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.

Explanation:

Take the following example:
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]

4 is prerequisite for both 1 and 2
1 is a prerequisite for 3
2 is a prerequisite for 3.

which can be visualised as a directed graph:

graph TD;
    4 --> 1;
    4 --> 2;
    2 --> 3;
    1 --> 3;

Which is equivalent to finding if a cycle exists in a directed graph. If a cycle exists,
then it is impossible to complete all courses.

"""

from collections import defaultdict
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    course_prequest_list = defaultdict(list)

    for prerequisite in prerequisites:
        course_prequest_list[prerequisite[0]].append(prerequisite[1])

    visited = [0] * num_courses

    def dfs(course: int):
        if visited[course] == 1:  # cycle detected
            return False
        if visited[course] == 2:  # already checked this course
            return True
        visited[course] = 1  # mark as being visited
        for neighbor in course_prequest_list.get(course, []):
            if not dfs(neighbor):
                return False
        visited[course] = 2  # mark as fully visited
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False
    return True
