from collections import OrderedDict
from datetime import datetime, timedelta
from typing import Hashable


class LRUCache:
    """Example implementation of LRU (least recently used) cache
    Don't use in Prod - use default library https://docs.python.org/3/library/functools.html#functools.lru_cache
    """

    def __init__(self, max_size: int = 10):
        self.cache = OrderedDict()
        self.max_size = max_size

    def put(self, key: Hashable, value):
        if key not in self.cache:
            if len(self.cache) >= self.max_size:
                # if capacity is reached, remove oldest item
                self.cache.popitem(last=False)

            self.cache[key] = value
        self.cache.move_to_end(key, last=True)

    def __setitem__(self, key: Hashable, value):
        self.put(key, value)

    def get(self, key: Hashable):
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]

    def __getitem__(self, key: Hashable):
        return self.get(key)

    def __iter__(self):
        for key in self.cache:
            yield key, self.cache[key]

    def __str__(self):
        return str(self.cache)


class TimeBoundedLRU(LRUCache):
    """Time bounded LRU (least recently used) cache - removes entries that have been inserted
    older than a specific time than a specific time"""

    def __init__(self, max_size=128, max_time: timedelta = timedelta(seconds=60)):
        super(TimeBoundedLRU, self).__init__(max_size)
        self.max_time = max_time

    def put(self, key, value):
        # Always update the key, as we want to keep the time consistent
        self.cache[key] = (value, datetime.now())
        self.cache.move_to_end(key=key, last=True)

        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)

        # Assume that we are going to have more reads than writes, so flush cache
        # only on put
        # as you can't mutate a ordered dict that your iterating over
        # make a copy
        new_cache = self.cache.copy()
        # Note if your using a list, there's a trick where you can iterate from the end
        # and pop (i.e. mutate) the list
        for key in self.cache:
            if datetime.now() - self.cache[key][1] >= self.max_time:
                new_cache.pop(key)
            else:
                break
        self.cache = new_cache

    def get(self, key: Hashable):
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key][0]

    def __iter__(self):
        for key in self.cache:
            yield key, self.cache[key][0]
