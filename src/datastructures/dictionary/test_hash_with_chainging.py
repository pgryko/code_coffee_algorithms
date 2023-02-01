import unittest

from hash_with_chaining import HashChaining


class TestHashChaining(unittest.TestCase):
    """
    Test initialisation of node class
    """

    def test_initialisation(self):
        hash_map = HashChaining()
        self.assertEqual(len(hash_map), 0)

    def test_put(self):
        hash_map = HashChaining()

        hash_map.put("AAA")

        self.assertTrue(hash_map.exists("AAA"))
        self.assertFalse(hash_map.exists("AAAB"))

    def test_chaining(self):
        hash_map = HashChaining()

        for i in range(20):
            hash_map.put(chr(i + 65))

        for i in range(20):
            self.assertTrue(hash_map.exists(chr(i + 65)))

        for i in range(20):
            self.assertFalse(hash_map.exists(chr(i + 85)))

    def test_delete(self):
        hash_map = HashChaining()

        with self.assertRaises(IndexError):
            hash_map.delete("AAA")

        for i in range(20):
            hash_map.put(chr(i + 65))

        self.assertTrue(hash_map.exists("A"))
        hash_map.delete("A")
        self.assertFalse(hash_map.exists("A"))
