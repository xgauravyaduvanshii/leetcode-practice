# LeetCode 2606. Find the Substring With Maximum Cost — Medium
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/
# Submission 2205099599 — Accepted, Python3
#
# My thinking: a letter costs its custom value when listed,
# else its alphabet position (a=1 .. z=26). Kadane's scan
# keeps the best substring ending here, resetting to zero
# whenever the running total goes negative — the empty
# substring costs 0, so the answer never goes below zero.
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        cost = {c: v for c, v in zip(chars, vals)}
        ans = cur = 0
        for ch in s:
            c = cost.get(ch, ord(ch) - 96)
            cur = max(0, cur + c)
            ans = max(ans, cur)
        return ans
