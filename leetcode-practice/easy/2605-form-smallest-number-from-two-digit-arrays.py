# LeetCode 2605. Form Smallest Number From Two Digit Arrays — Easy
# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/
# Submission 2197809148 — Accepted, Python3
#
# My thinking: if the two arrays share a digit, the
# smallest shared digit alone is the answer.
# Otherwise I take the smallest digit from each
# array and put the smaller one first to form a
# two-digit number.

class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        common = set(nums1) & set(nums2)
        if common:
            return min(common)
        d1 = min(nums1)
        d2 = min(nums2)
        return min(d1, d2) * 10 + max(d1, d2)
