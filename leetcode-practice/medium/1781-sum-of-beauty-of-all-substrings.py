# LeetCode 1781. Sum of Beauty of All Substrings — Medium
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
# Submission 2199933848 — Accepted, Python3
#
# My thinking: a substring's beauty is its
# most common letter count minus its least
# common. I grow every substring from each
# start, keeping a running count of its
# letters.

from collections import Counter


class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            counts = Counter()
            for j in range(i, len(s)):
                counts[s[j]] += 1
                values = counts.values()
                total += max(values) - min(values)
        return total
