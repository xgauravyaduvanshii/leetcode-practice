# LeetCode 2570. Merge Two 2D Arrays by Summing Values — Easy
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
# Submission 2197804880 — Accepted, Python3
#
# My thinking: I add up the values for each id in a
# dictionary, then read the ids out in sorted order
# with their totals.

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i, v in nums1:
            d[i] = d.get(i, 0) + v
        for i, v in nums2:
            d[i] = d.get(i, 0) + v
        return [[i, d[i]] for i in sorted(d)]
