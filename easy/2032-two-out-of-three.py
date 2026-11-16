# LeetCode 2032. Two Out of Three — Easy
# https://leetcode.com/problems/two-out-of-three/
# Submission 2197609885 — Accepted, Python3
#
# My thinking: a number counts when it appears in at
# least two of the three arrays. I turn each array
# into a set and take the union of the three
# pairwise intersections. (The run output [2, 3]
# differed in order from the expected [3, 2], but
# any order is accepted.)

class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return list((s1 & s2) | (s2 & s3) | (s1 & s3))
