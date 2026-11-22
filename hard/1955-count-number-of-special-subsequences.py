# LeetCode 1955. Count Number of Special Subsequences — Hard
# https://leetcode.com/problems/count-number-of-special-subsequences/
# Submission 2201268764 — Accepted, Python3
#
# My thinking: I count the subsequences that are
# some 0s, then some 1s, then some 2s — each new
# number either doubles the count so far or starts
# a fresh run from the stage before it.

class Solution:
    def countSpecialSubsequences(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        dp0 = dp1 = dp2 = 0
        for x in nums:
            if x == 0:
                dp0 = (dp0 * 2 + 1) % MOD
            elif x == 1:
                dp1 = (dp1 * 2 + dp0) % MOD
            else:
                dp2 = (dp2 * 2 + dp1) % MOD
        return dp2
