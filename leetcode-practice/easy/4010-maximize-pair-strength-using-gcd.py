# 4010. Maximize Pair Strength Using GCD (Easy)
# https://leetcode.com/problems/maximize-pair-strength-using-gcd/
# Submission 2200097349 — Accepted, Python3
from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        # My thinking: the strength of a pair is its
        # product divided by the square of their gcd.
        # I try every pair and keep the best.
        best = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                g = gcd(nums[i], nums[j])
                best = max(best, (nums[i] * nums[j]) // (g * g))
        return best
