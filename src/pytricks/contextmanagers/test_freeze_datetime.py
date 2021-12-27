import unittest
from freeze_datetime import FreezeDateTime
import datetime


class TestFreezeDatetime(unittest.TestCase):

    def test_freeze(self):
        with FreezeDateTime(datetime.datetime(2012, 1, 14, 12, 0, 1)):
            self.assertEqual(datetime.datetime.now(), datetime.datetime(2012, 1, 14, 12, 0, 1))

        with FreezeDateTime(datetime.datetime(2014, 1, 14, 12, 0, 1)):
            self.assertEqual(datetime.datetime.now(), datetime.datetime(2014, 1, 14, 12, 0, 1))

        self.assertNotEqual(datetime.datetime.now(), datetime.datetime(2014, 1, 14, 12, 0, 1))
