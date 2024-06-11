import unittest

from course_schedual import can_finish_dfs


class CanFinishTestCase(unittest.TestCase):
    def test_canFinish_withValidCourseOrder_shouldReturnTrue(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2]]
        self.assertTrue(can_finish_dfs(numCourses, prerequisites))

    def test_canFinish_withValidCourseOrder_shouldReturnTrue_2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1]]
        self.assertTrue(can_finish_dfs(numCourses, prerequisites))

    def test_canFinish_withInvalidCourseOrder_shouldReturnFalse(self):
        numCourses = 4
        prerequisites = [[1, 0], [0, 1], [3, 2]]
        self.assertFalse(can_finish_dfs(numCourses, prerequisites))

    def test_canFinish_withNoPrerequisites_shouldReturnTrue(self):
        numCourses = 3
        prerequisites = []
        self.assertTrue(can_finish_dfs(numCourses, prerequisites))

    def test_canFinish_withSingleCourse_shouldReturnTrue(self):
        numCourses = 1
        prerequisites = []
        self.assertTrue(can_finish_dfs(numCourses, prerequisites))

    def test_canFinish_withCircularDependency_shouldReturnFalse(self):
        numCourses = 3
        prerequisites = [[0, 1], [1, 2], [2, 0]]
        self.assertFalse(can_finish_dfs(numCourses, prerequisites))
