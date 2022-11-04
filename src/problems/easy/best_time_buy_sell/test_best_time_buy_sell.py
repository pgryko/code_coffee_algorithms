import unittest

from best_time_buy_sell import optimize_buy_sell


class TestBestTimeBuySell(unittest.TestCase):
    def test_prices_1(self):
        self.assertEqual(optimize_buy_sell([7, 1, 5, 3, 6, 4]), 5)

    def test_prices_2(self):
        self.assertEqual(optimize_buy_sell([7, 6, 4, 3, 1]), 0)
