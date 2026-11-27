# LeetCode 1799. Maximize Score After N Operations — Hard
# https://leetcode.com/problems/maximize-score-after-n-operations/
# Submission 2201169552 — Accepted, Python3
#
# My thinking: I remember which numbers are already
# used as a bitmask, and at each step I try every
# unused pair — the pair's score is the operation
# number times the gcd of the two numbers.

from math import gcd

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)
        m = 1 << n
        dp = [0] * m
        for mask in range(m):
            bits = bin(mask).count("1")
            if bits % 2 == 1:
                continue
            op = bits // 2 + 1
            for i in range(n):
                if mask & (1 << i):
                    continue
                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue
                    nmask = mask | (1 << i) | (1 << j)
                    dp[nmask] = max(dp[nmask], dp[mask] + op * gcd(nums[i], nums[j]))
        return dp[m - 1]
