# LeetCode 1770. Maximum Score from Performing Multiplication Operations — Hard
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
# Submission 2201153442 — Accepted, Python3
#
# My thinking: after some operations I have taken
# a few numbers from the left and the rest from the
# right, so I only need to remember how many came
# from the left — each new multiplier can take the
# next number from either end.

class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        neg = float("-inf")
        dp = [neg] * (m + 1)
        dp[0] = 0
        for op in range(m):
            ndp = [neg] * (m + 1)
            for left in range(op + 1):
                if dp[left] == neg:
                    continue
                right = op - left
                ndp[left + 1] = max(ndp[left + 1], dp[left] + multipliers[op] * nums[left])
                ndp[left] = max(ndp[left], dp[left] + multipliers[op] * nums[n - 1 - right])
            dp = ndp
        return max(dp)
