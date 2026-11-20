# 3131. Find the Integer Added to Array I (Easy)
# https://leetcode.com/problems/find-the-integer-added-to-array-i/
# Submission 2199978884 — Accepted, Python3
from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # My thinking: after sorting, each number in the
        # second list is the matching number from the
        # first list plus the same hidden amount — so the
        # gap between the two smallest numbers is that
        # amount.
        return min(nums2) - min(nums1)
