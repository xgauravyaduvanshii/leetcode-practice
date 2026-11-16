# LeetCode 941. Valid Mountain Array — Easy
# https://leetcode.com/problems/valid-mountain-array/
# Submission 2197544718 — Accepted, Python3
#
# My thinking: I climb up while the numbers keep
# rising, then climb down while they keep falling.
# It is a mountain only if I actually climbed up
# (not flat at the start), came down again, and
# reached the very end.

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1
