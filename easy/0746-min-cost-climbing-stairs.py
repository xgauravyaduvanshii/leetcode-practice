# LeetCode 746. Min Cost Climbing Stairs — Easy
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Submission 2197523933 — Accepted, Python3
#
# My thinking: to reach each step, I come from one
# or two steps below — whichever was cheaper. So I
# build up the cheapest cost to reach every step in
# turn, and the answer is the cheapest cost to
# reach the top, one past the last step.

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
