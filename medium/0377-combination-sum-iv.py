# LeetCode 377. Combination Sum IV — Medium
# https://leetcode.com/problems/combination-sum-iv/
# Submission 2198764584 — Accepted, Python3
#
# My thinking: the number of ways to reach a total
# is the sum of the ways to reach the totals left
# after one last number. I build that up from zero
# — order matters here, so every number gets its
# turn as the last one.

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for total in range(1, target + 1):
            for num in nums:
                if num <= total:
                    dp[total] += dp[total - num]
        return dp[target]
