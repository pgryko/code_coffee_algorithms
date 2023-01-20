import unittest

from src.problems.medium.insert_interval.insert_interval import insert_interval


class TestInsertInterval(unittest.TestCase):
    def test_single_overlapping_region(self):

        self.assertEqual(
            insert_interval(intervals=[[1, 3], [6, 7], [8, 10]], newInterval=[2, 5]),
            [[1, 5], [6, 7], [8, 10]],
        )

    #
    # def test_single_non_overlapping_region(self):
    #
    #     self.assertEqual(
    #         insert_interval(intervals=[[1, 3], [6, 7], [8, 10]], newInterval=[2, 5]),
    #         [[1, 3], [2, 5], [6, 7], [8, 10]],
    #     )
