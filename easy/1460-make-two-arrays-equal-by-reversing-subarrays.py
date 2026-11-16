# LeetCode 1460. Make Two Arrays Equal by Reversing Subarrays — Easy
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
# Submission 2197580282 — Accepted, Python3
#
# My thinking: reversing any subarray lets me
# rearrange the numbers freely, so the two arrays
# can be made equal exactly when they contain the
# same numbers — that is, when their sorted forms
# are identical.

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return sorted(target) == sorted(arr)
