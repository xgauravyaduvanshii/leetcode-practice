# LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee — Medium
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# Submission 2198918216 — Accepted, Python3
#
# My thinking: I track the best I can do holding
# cash and holding a share. Each day I either sell
# — paying the fee — or buy again, keeping
# whichever leaves me richer.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash
