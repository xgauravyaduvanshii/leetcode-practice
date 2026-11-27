# LeetCode 1818. Minimum Absolute Sum Difference — Medium
# https://leetcode.com/problems/minimum-absolute-sum-difference/
# Submission 2199941415 — Accepted, Python3
#
# My thinking: replacing one element can only
# shrink its own gap, so I check the best
# replacement for every position — the sorted
# array's nearest neighbours to the target —
# and keep the biggest single saving.

import bisect
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10 ** 9 + 7
        total = sum(abs(a - b) for a, b in zip(nums1, nums2))
        sorted_nums1 = sorted(nums1)
        best_gain = 0
        for a, b in zip(nums1, nums2):
            pos = bisect.bisect_left(sorted_nums1, b)
            for neighbour in (pos, pos - 1):
                if 0 <= neighbour < len(sorted_nums1):
                    gain = abs(a - b) - abs(sorted_nums1[neighbour] - b)
                    best_gain = max(best_gain, gain)
        return (total - best_gain) % mod
