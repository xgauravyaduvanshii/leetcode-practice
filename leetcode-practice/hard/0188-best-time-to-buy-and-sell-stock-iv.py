# LeetCode 188. Best Time to Buy and Sell Stock IV — Hard
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Submission 2198393051 — Accepted, Python3
#
# My thinking: I keep, for each allowed trade, the
# best result after buying and after selling so
# far, and update them price by price. When k is
# big enough to cover every rise, I simply add up
# all the upward moves instead — the trade limit
# stops mattering then.

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or n < 2:
            return 0
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))
        buy = [float("-inf")] * k
        sell = [0] * k
        for price in prices:
            for t in range(k):
                prev_sell = sell[t - 1] if t > 0 else 0
                buy[t] = max(buy[t], prev_sell - price)
                sell[t] = max(sell[t], buy[t] + price)
        return sell[-1]
