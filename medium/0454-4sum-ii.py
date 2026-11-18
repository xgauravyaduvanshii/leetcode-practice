# LeetCode 454. 4Sum II — Medium
# https://leetcode.com/problems/4sum-ii/
# Submission 2198805652 — Accepted, Python3
#
# My thinking: I count every sum of a pair from the
# first two arrays, then for each pair from the last
# two arrays I look up how many first pairs cancel
# it out. The two halves meet in the middle.

from collections import Counter
from typing import List


class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int],
    ) -> int:
        pair_sums = Counter(a + b for a in nums1 for b in nums2)
        return sum(pair_sums[-(c + d)] for c in nums3 for d in nums4)
