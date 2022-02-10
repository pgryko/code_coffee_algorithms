import unittest

from freezegun import freeze_time

from lru_cache import LRUCache, TimeBoundedLRU


class TestLRUCache(unittest.TestCase):
    def test_constructor(self):
        # Should not throw
        cache = LRUCache()

    def test_simple(self):
        cache = LRUCache(max_size=2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        # Expect eviction of 2,2
        cache.put(3, 3)
        self.assertIsNone(cache.get(2))
        # Evict 1
        cache.put(4, 4)
        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_setter_getter(self):
        cache = LRUCache(max_size=2)
        cache[1] = 1
        cache[2] = 2
        self.assertEqual(cache[1], 1)
        # Expect eviction of 2,2
        cache[3] = 3
        self.assertIsNone(cache[2])
        # Evict 1
        cache[4] = 4
        self.assertIsNone(cache[1])
        self.assertEqual(cache[3], 3)
        self.assertEqual(cache[4], 4)
        # Test implementation of __iter__ by exporting as dict
        self.assertDictEqual(dict(cache), {4: 4, 3: 3})


class TestTimeBoundedLRUCache(unittest.TestCase):
    def test_constructor(self):
        # Should not throw
        cache = TimeBoundedLRU()

    def test_simple(self):
        cache = TimeBoundedLRU(max_size=2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        # Expect eviction of 2,2
        cache.put(3, 3)
        self.assertIsNone(cache.get(2))
        # Evict 1
        cache.put(4, 4)
        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_setter_getter(self):
        cache = TimeBoundedLRU(max_size=2)
        cache[1] = 1
        cache[2] = 2
        self.assertEqual(cache[1], 1)
        # Expect eviction of 2,2
        cache[3] = 3
        self.assertIsNone(cache[2])
        # Evict 1
        cache[4] = 4
        self.assertIsNone(cache[1])
        self.assertEqual(cache[3], 3)
        self.assertEqual(cache[4], 4)
        # Test implementation of __iter__ by exporting as dict
        self.assertDictEqual(dict(cache), {4: 4, 3: 3})

    def test_time_bounding(self):
        cache = TimeBoundedLRU(max_size=20)
        with freeze_time("2012-01-14 12:00:01"):
            cache[1] = 1
        with freeze_time("2012-01-14 12:00:02"):
            cache[2] = 2
        with freeze_time("2012-01-14 12:00:32"):
            cache[3] = 3
        with freeze_time("2012-01-14 12:00:52"):
            cache[4] = 4
        self.assertDictEqual(dict(cache), {4: 4, 3: 3, 2: 2, 1: 1})

        with freeze_time("2012-01-14 12:01:02"):
            cache[5] = 5

        self.assertDictEqual(dict(cache), {5: 5, 4: 4, 3: 3})
