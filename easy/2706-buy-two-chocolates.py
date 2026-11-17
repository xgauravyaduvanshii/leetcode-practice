# LeetCode 2706. Buy Two Chocolates — Easy
# https://leetcode.com/problems/buy-two-chocolates/
# Submission 2197819292 — Accepted, Python3
#
# My thinking: the cheapest way to buy two
# chocolates is to take the two cheapest prices.
# If I can afford them, the leftover money is the
# answer; otherwise I keep all my money.

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        s = prices[0] + prices[1]
        return money - s if s <= money else money
