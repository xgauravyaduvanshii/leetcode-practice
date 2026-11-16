# LeetCode 594. Longest Harmonious Subsequence — Easy
# https://leetcode.com/problems/longest-harmonious-subsequence/
# Submission 2197502748 — Accepted, Python3
#
# My thinking: a harmonious subsequence only uses two
# numbers that differ by exactly 1, so it is just a
# pair of neighbouring values. I count how many of
# each number there are, then try every pair of
# neighbours and keep the biggest total.

from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)
        best = 0
        for num, count in counts.items():
            if num + 1 in counts:
                best = max(best, count + counts[num + 1])
        return best
