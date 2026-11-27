# LeetCode 2956. Find Common Elements Between Two Arrays — Easy
# https://leetcode.com/problems/find-common-elements-between-two-arrays/
# Submission 2198704256 — Accepted, Python3
#
# My thinking: I turn both arrays into sets, then
# count how many entries of the first array appear in
# the second set, and how many entries of the second
# appear in the first set.

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        return [
            sum(1 for x in nums1 if x in set2),
            sum(1 for x in nums2 if x in set1),
        ]
