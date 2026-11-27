# LeetCode 121. Best Time to Buy and Sell Stock — Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Submission 2197442873 — Accepted, Python3
#
# My thinking: I only need the cheapest price I have
# seen so far. Every day I check: if today is cheaper,
# that becomes my new buy price. Otherwise, selling
# today would give me today's price minus that cheapest
# price — if that is better than my best profit so far,
# I keep it.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheapest = float('inf')
        best_profit = 0
        for price in prices:
            if price < cheapest:
                cheapest = price
            elif price - cheapest > best_profit:
                best_profit = price - cheapest
        return best_profit
