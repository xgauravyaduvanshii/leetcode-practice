# LeetCode 2654. Minimum Number of Operations to Make All Array Elements Equal to 1 — Medium
# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
# Submission 2205112060 — Accepted, Python3
#
# My thinking: one operation replaces an element by the gcd
# with its neighbour, so a 1 can only spread from a subarray
# whose gcd is 1. If the array is all 1s, nothing to do; if
# some 1s exist, spread them (n - ones operations). Otherwise
# first build a 1 inside the shortest gcd-1 subarray (its
# length minus one operations), then spread it (n - 1 more).
# No gcd-1 subarray means it is impossible.
import math


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones == n:
            return 0
        if ones > 0:
            return n - ones
        best = math.inf
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break
        if best == math.inf:
            return -1
        return (best - 1) + (n - 1)
