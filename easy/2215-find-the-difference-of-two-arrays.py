# LeetCode 2215. Find the Difference of Two Arrays — Easy
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Submission 2197618241 — Accepted, Python3
#
# My thinking: I turn both arrays into sets and take
# the two differences — what is in the first but not
# the second, and what is in the second but not the
# first.

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
