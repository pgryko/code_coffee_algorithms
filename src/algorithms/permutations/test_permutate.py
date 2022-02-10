import unittest
import itertools
from math import factorial

from permutate import permutate


class TestPermutate(unittest.TestCase):
    def test_permutate(self):

        map = set()

        count = 0

        for element in permutate(["a", "b", "c", "d"]):
            map.add(tuple(element))
            count += 1

        # Test against built in type - normally we'd test against hardcoded
        # list of values
        for elem in itertools.permutations(["a", "b", "c", "d"]):
            self.assertIn(elem, map)

        # Test that the algorithm generated the correct no of permutations (i.e. no extras)
        self.assertEqual(count, factorial(4))


if __name__ == "__main__":
    unittest.main()
