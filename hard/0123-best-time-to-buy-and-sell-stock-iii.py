# LeetCode 123. Best Time to Buy and Sell Stock III — Hard
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# Submission 2198385392 — Accepted, Python3
#
# My thinking: at most two trades, so I track four
# numbers as I walk the prices — the best I can do
# after the first buy, after the first sell, after
# the second buy, and after the second sell. Each
# price updates them in order, and the last one is
# the answer. Starting the buys at minus infinity
# means no trade is forced when prices only fall.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2
