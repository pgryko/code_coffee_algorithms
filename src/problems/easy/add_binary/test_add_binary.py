import unittest

from add_binary import add_binary


class TestAddBinary(unittest.TestCase):
    def test_add_binary(self):
        self.assertEqual(add_binary("11", "1"), "100")
        self.assertEqual(add_binary("1010", "1011"), "10101")

        # Test inputs with equal lengths
        self.assertEqual(add_binary("101", "100"), "1001")
        self.assertEqual(add_binary("111", "111"), "1110")
        self.assertEqual(add_binary("010", "010"), "100")

        # Test inputs with different lengths
        self.assertEqual(add_binary("1", "111"), "1000")
        self.assertEqual(add_binary("111", "1"), "1000")

        # Test input with carry
        self.assertEqual(add_binary("11", "11"), "110")
