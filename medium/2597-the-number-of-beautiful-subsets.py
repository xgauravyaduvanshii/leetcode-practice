# LeetCode 2597. The Number of Beautiful Subsets — Medium
# https://leetcode.com/problems/the-number-of-beautiful-subsets/
# Submission 2205095503 — Accepted, Python3
#
# My thinking: two numbers conflict only when they differ by k,
# so split by value modulo k — groups never interact. Inside a
# group the values form chains spaced by k; walk each chain
# like house-robber counting, where taking a value contributes
# (2^freq - 1) choices and blocks its chain neighbour. Multiply
# the group totals and subtract the empty subset.
from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        groups = defaultdict(list)
        for x in nums:
            groups[x % k].append(x)
        total = 1
        for g in groups.values():
            freq = defaultdict(int)
            for x in g:
                freq[x] += 1
            vals = sorted(freq)
            dp_prev2, dp_prev1 = 1, 1
            prev = None
            for v in vals:
                ways = (1 << freq[v]) - 1
                if prev is not None and v - prev == k:
                    cur = dp_prev1 + dp_prev2 * ways
                else:
                    cur = dp_prev1 * (ways + 1)
                dp_prev2, dp_prev1 = dp_prev1, cur
                prev = v
            total *= dp_prev1
        return total - 1
