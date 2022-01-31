import unittest

from isunique import isunique

class TestIsUnique(unittest.TestCase):

    def test_isunique(self):
        # Test Empty string
        self.assertTrue(isunique(''))
        self.assertTrue(isunique('AB34'))
        self.assertFalse(isunique('AB34A'))
        self.assertFalse(isunique('AAB34'))
