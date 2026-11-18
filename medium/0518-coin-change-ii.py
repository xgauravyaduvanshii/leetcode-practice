# LeetCode 518. Coin Change II — Medium
# https://leetcode.com/problems/coin-change-ii/
# Submission 2198838206 — Accepted, Python3
#
# My thinking: I count combinations, not orders, so
# I take the coins one denomination at a time and
# let each one fill every amount it can reach. That
# way each combination is counted exactly once.

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for total in range(coin, amount + 1):
                dp[total] += dp[total - coin]
        return dp[amount]
