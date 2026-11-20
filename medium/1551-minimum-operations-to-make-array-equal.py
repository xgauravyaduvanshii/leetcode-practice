# LeetCode 1551. Minimum Operations to Make Array Equal — Medium
# https://leetcode.com/problems/minimum-operations-to-make-array-equal/
# Submission 2199874936 — Accepted, Python3
#
# My thinking: the array is 1, 3, 5, and so
# on, so everything must meet at the middle
# value. The moves add up to a quarter of n
# squared.

class Solution:
    def minOperations(self, n: int) -> int:
        return (n * n) // 4
