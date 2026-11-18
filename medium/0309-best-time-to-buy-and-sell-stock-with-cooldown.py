# LeetCode 309. Best Time to Buy and Sell Stock with Cooldown — Medium
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Submission 2198738482 — Accepted, Python3
#
# My thinking: each day I track three states — holding
# a share, just sold, or resting. Holding comes from
# holding on or buying after a rest, resting comes
# from resting on or the cooldown after a sale, and
# selling comes from yesterday's hold plus today's
# price. The best ending is sold or resting.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0
        for price in prices[1:]:
            previous_hold = hold
            hold = max(hold, rest - price)
            rest = max(rest, sold)
            sold = previous_hold + price
        return max(sold, rest)
