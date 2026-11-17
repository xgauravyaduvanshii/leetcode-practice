# LeetCode 2404. Most Frequent Even Element — Easy
# https://leetcode.com/problems/most-frequent-even-element/
# Submission 2197779729 — Accepted, Python3
#
# My thinking: I count only the even numbers. The
# answer is the one with the highest count, and if
# several tie, the smallest one. If there is no even
# number at all, the answer is -1.

from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        counts = Counter(x for x in nums if x % 2 == 0)
        if not counts:
            return -1
        return min(counts, key=lambda x: (-counts[x], x))
