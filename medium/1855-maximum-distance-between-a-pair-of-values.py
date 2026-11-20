# 1855. Maximum Distance Between a Pair of Values (Medium)
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
# Submission 2199950361 — Accepted, Python3
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # My thinking: both arrays are non-increasing, so
        # when we move to a smaller value in nums1, even
        # more values in nums2 become big enough. A single
        # pointer walks through nums2 once; for every i we
        # remember the farthest j that still works.
        n, m = len(nums1), len(nums2)
        best = 0
        j = 0
        for i in range(n):
            while j < m and nums2[j] >= nums1[i]:
                j += 1
            # j - 1 is the farthest index that still works
            # for this i (if it is not behind i).
            best = max(best, j - 1 - i)
        return best
