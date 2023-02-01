import unittest

from src.problems.medium.insert_interval.insert_interval import (
    insert_interval,
    overlap,
    merge_interval,
)


class TestInsertIntervalAncillaryFunctions(unittest.TestCase):
    def test_overlap_true(self):
        # Directly overlap
        self.assertTrue(overlap((3, 5), (4, 6)))
        self.assertTrue(overlap((4, 6), (3, 5)))

        # Overlap on edges
        self.assertTrue(overlap((3, 5), (5, 6)))
        self.assertTrue(overlap((5, 6), (3, 5)))

        # Overlap completely
        self.assertTrue(overlap((3, 8), (4, 5)))
        self.assertTrue(overlap((4, 5), (3, 8)))

    def test_overlap_false(self):
        self.assertTrue(overlap((3, 5), (4, 6)))
        self.assertTrue(overlap((4, 6), (3, 5)))

    def test_merge_intervals(self):
        # Directly overlap
        self.assertEqual(merge_interval((3, 5), (4, 6)), (3, 6))
        self.assertEqual(merge_interval((4, 6), (3, 5)), (3, 6))

        # Overlap on edges
        self.assertEqual(merge_interval((3, 5), (5, 6)), (3, 6))
        self.assertEqual(merge_interval((5, 6), (3, 5)), (3, 6))

        # Overlap completely
        self.assertEqual(merge_interval((3, 8), (4, 5)), (3, 8))
        self.assertEqual(merge_interval((4, 5), (3, 8)), (3, 8))


class TestInsertInterval(unittest.TestCase):
    # Test cases with non overlapping intervals
    def test_insert_front(self):
        # Test inserting element on front of list
        self.assertEqual(
            insert_interval(intervals=[(3, 5), (6, 7), (8, 10)], new_interval=(1, 2)),
            [(1, 2), (3, 5), (6, 7), (8, 10)],
        )

        # Test inserting element on front of list that overlaps one
        self.assertEqual(
            insert_interval(intervals=[(3, 5), (6, 7), (8, 10)], new_interval=(1, 4)),
            [(1, 5), (6, 7), (8, 10)],
        )

        # Test inserting element on front of list that overlaps multiple
        self.assertEqual(
            insert_interval(intervals=[(3, 5), (6, 7), (8, 10)], new_interval=(1, 6)),
            [(1, 7), (8, 10)],
        )

        # Test inserting element on front of list that overlaps all
        self.assertEqual(
            insert_interval(intervals=[(3, 5), (6, 7), (8, 10)], new_interval=(1, 11)),
            [(1, 11)],
        )

    def test_insert_end(self):
        # Test inserting element on end of list
        self.assertEqual(
            insert_interval(intervals=[(3, 5), (6, 7), (8, 10)], new_interval=(11, 12)),
            [(3, 5), (6, 7), (8, 10), (11, 12)],
        )

        # Test inserting element on end of list overlaping
        self.assertEqual(
            insert_interval(intervals=[(3, 5), (6, 7), (8, 10)], new_interval=(10, 12)),
            [(3, 5), (6, 7), (8, 12)],
        )

    def test_insert_non_overlapping(self):
        self.assertEqual(
            insert_interval(intervals=[(1, 2), (6, 7), (8, 10)], new_interval=(3, 5)),
            [(1, 2), (3, 5), (6, 7), (8, 10)],
        )

        self.assertEqual(
            insert_interval(intervals=[(1, 2), (3, 5), (8, 10)], new_interval=(6, 7)),
            [(1, 2), (3, 5), (6, 7), (8, 10)],
        )

    def test_insert_overlapping(self):
        self.assertEqual(
            insert_interval(intervals=[(3, 5), (6, 7), (8, 10)], new_interval=(3, 4)),
            [(3, 5), (6, 7), (8, 10)],
        )

        self.assertEqual(
            insert_interval(intervals=[(3, 5), (7, 8), (9, 10)], new_interval=(3, 6)),
            [(3, 6), (7, 8), (9, 10)],
        )

        self.assertEqual(
            insert_interval(intervals=[(3, 5), (7, 8), (9, 10)], new_interval=(6, 7)),
            [(3, 5), (6, 8), (9, 10)],
        )

        self.assertEqual(
            insert_interval(intervals=[(3, 5), (7, 8), (9, 10)], new_interval=(6, 10)),
            [(3, 5), (6, 10)],
        )
