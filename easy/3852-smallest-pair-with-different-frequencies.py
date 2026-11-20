# 3852. Smallest Pair With Different Frequencies (Easy)
# https://leetcode.com/problems/smallest-pair-with-different-frequencies/
# Submission 2200073964 — Accepted, Python3
from collections import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        # My thinking: take the values in order. For
        # the smallest value, the smallest bigger value
        # with a different count is the best partner —
        # and the first value that has any partner at
        # all is the answer.
        counts = Counter(nums)
        values = sorted(counts)
        for i, x in enumerate(values):
            for y in values[i + 1:]:
                if counts[y] != counts[x]:
                    return [x, y]
        return [-1, -1]
