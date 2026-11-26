# LeetCode 122. Best Time to Buy and Sell Stock II — Medium
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Submission 2204018463 — Accepted, Python3
#
# My thinking:
# We can buy and sell as many times as we like, but we must sell before
# buying again, and we can only hold one share at a time.
# Any climb in the price can be captured: if the price goes up from one
# day to the next, buying on the first day and selling on the second
# pockets that gain. A longer climb is just a chain of these one-day
# gains added together (buying low and selling high over several days
# earns exactly the same as adding up each daily rise in between).
# So the best total profit is simply the sum of every positive
# day-to-day price increase. Days where the price falls add nothing,
# since we just do not trade on them.
# This is a single pass through the prices, O(n) time and O(1) space.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
