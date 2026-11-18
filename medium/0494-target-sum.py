# LeetCode 494. Target Sum — Medium
# https://leetcode.com/problems/target-sum/
# Submission 2198830274 — Accepted, Python3
#
# My thinking: putting a plus in front of some
# numbers and a minus in front of the rest is the
# same as choosing a subset that adds up to half of
# (total + target). I count those subsets with a
# knapsack, one number at a time.

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 == 1 or abs(target) > total:
            return 0
        subset_sum = (total + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[subset_sum]
