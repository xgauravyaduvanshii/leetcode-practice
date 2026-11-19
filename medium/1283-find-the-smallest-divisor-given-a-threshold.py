# LeetCode 1283. Find the Smallest Divisor Given a Threshold — Medium
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
# Submission 2199023211 — Accepted, Python3
#
# My thinking: a bigger divisor only shrinks
# the rounded-up sum, so the answer is the
# smallest divisor whose sum fits the threshold
# — found with a binary search.

import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(math.ceil(value / mid) for value in nums) <= threshold:
                hi = mid
            else:
                lo = mid + 1
        return lo
