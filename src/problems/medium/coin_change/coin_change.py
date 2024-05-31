"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:

    # We do amount + 1, as we want to account for disa
    distance_per_amount = [amount + 1] * (amount + 1)

    distance_per_amount[0] = 0

    for coin in coins:
        for value in range(coin, amount + 1):
            distance_per_amount[value] = min(
                distance_per_amount[value], distance_per_amount[value - coin] + 1
            )

    if distance_per_amount[amount] == amount + 1:
        return -1
    return distance_per_amount[amount]


if __name__ == "__main__":

    print(coin_change(coins=[1, 2, 5], amount=11))
