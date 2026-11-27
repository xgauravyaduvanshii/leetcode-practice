# LeetCode 2540. Minimum Common Value — Easy
# https://leetcode.com/problems/minimum-common-value/
# Submission 2197800311 — Accepted, Python3
#
# My thinking: both arrays are sorted, so the first
# value of the first array that also appears in the
# second is the smallest common value. If none
# appears, the answer is -1.

class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        s2 = set(nums2)
        for x in nums1:
            if x in s2:
                return x
        return -1
