# LeetCode 322. Coin Change — Medium
# https://leetcode.com/problems/coin-change/
# Submission 2198745862 — Accepted, Python3
#
# My thinking: the fewest coins for an amount is one
# more than the fewest coins for the amount left
# after one coin. I build that up from zero, trying
# every coin at each step, and -1 when an amount
# stays unreachable.

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for target in range(1, amount + 1):
            for coin in coins:
                if coin <= target:
                    dp[target] = min(dp[target], dp[target - coin] + 1)
        return -1 if dp[amount] == float("inf") else dp[amount]
