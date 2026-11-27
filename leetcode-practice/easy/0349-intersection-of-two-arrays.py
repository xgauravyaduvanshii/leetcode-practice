# LeetCode 349. Intersection of Two Arrays — Easy
# https://leetcode.com/problems/intersection-of-two-arrays/
# Submission 2197466410 — Accepted, Python3
#
# My thinking: if I turn both lists into sets, the
# numbers that appear in both are just the set
# intersection. Duplicates disappear automatically.

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
