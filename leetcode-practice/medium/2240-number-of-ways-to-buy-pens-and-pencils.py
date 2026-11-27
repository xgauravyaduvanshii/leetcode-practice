# LeetCode 2240. Number of Ways to Buy Pens and Pencils — Medium
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/
# Submission 2204513073 — Accepted, Python3
#
# My thinking: for each possible number of pens I can afford, the
# remaining money buys between 0 and the affordable number of pencils,
# which is one count per pencil quantity. I add that count for every
# pen quantity from zero up to the most I can afford.
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        pens = 0
        while pens * cost1 <= total:
            ans += (total - pens * cost1) // cost2 + 1
            pens += 1
        return ans
