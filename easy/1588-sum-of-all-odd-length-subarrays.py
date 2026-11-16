# LeetCode 1588. Sum of All Odd Length Subarrays — Easy
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Submission 2197588132 — Accepted, Python3
#
# My thinking: each element appears in a certain
# number of subarrays — (i + 1) choices for the
# left end times (n - i) for the right end. About
# half of those have odd length, and the exact
# count is ((i + 1) * (n - i) + 1) // 2. I multiply
# each element by how many odd-length subarrays it
# sits in and add it all up.

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        total = 0
        for i, x in enumerate(arr):
            total += x * (((i + 1) * (n - i) + 1) // 2)
        return total
