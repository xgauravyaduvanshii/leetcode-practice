# LeetCode 2335. Minimum Amount of Time to Fill Cups — Easy
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
# Submission 2197623462 — Accepted, Python3
#
# My thinking: each second I can fill at most two
# cups, so the time is at least half the total cups
# rounded up — but it can never be less than the
# biggest single type, since one cup of that type
# takes one second each.

class Solution:
    def fillCups(self, amount: list[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)
