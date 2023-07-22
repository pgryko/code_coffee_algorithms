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
from collections import defaultdict, deque
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)

    #  'prequisites_list' is a list where the value at each index is the number of prerequisites
    #  for the course at that index
    prequisites_list = [0] * numCourses

    for x, y in prerequisites:
        # Note we do graph 'y'
        graph[y].append(x)
        # Note we do prequisites_list 'x'
        prequisites_list[x] += 1

    # queue initially contains all the courses that have no prerequisites
    queue = deque([i for i in range(numCourses) if prequisites_list[i] == 0])

    while queue:
        course = queue.popleft()
        for next_course in graph[course]:
            prequisites_list[next_course] -= 1
            # If any dependent course's in-degree reaches zero (meaning all its prerequisites have been taken),
            # we add it to the queue
            if prequisites_list[next_course] == 0:
                queue.append(next_course)

    # if every course's in-degree is 0 (meaning every course can be taken), then we return True
    return sum(prequisites_list) == 0
