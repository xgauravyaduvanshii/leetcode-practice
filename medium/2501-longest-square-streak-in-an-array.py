# LeetCode 2501. Longest Square Streak in an Array — Medium
# https://leetcode.com/problems/longest-square-streak-in-an-array/
# Submission 2204976415 — Accepted, Python3
#
# My thinking: sort the distinct numbers and build chains upwards:
# a number continues a chain when its square root is already in a
# chain, giving one more than the root's chain length. The longest
# chain is the answer, or -1 when no chain reaches length 2.
import math


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        dp = {}
        res = 0
        for x in sorted(set(nums)):
            r = math.isqrt(x)
            if r * r == x and r in dp:
                dp[x] = dp[r] + 1
            else:
                dp[x] = 1
            res = max(res, dp[x])
        return res if res >= 2 else -1
