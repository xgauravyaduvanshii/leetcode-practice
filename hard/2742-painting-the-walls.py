# LeetCode 2742. Painting the Walls — Hard
# https://leetcode.com/problems/painting-the-walls/
# Submission 2201878983 — Accepted, Python3
#
# My thinking: every wall I pay for
# covers itself and buys the free
# painter that many more walls of time,
# so the whole job is a knapsack — I
# pick the cheapest set of paid walls
# whose own count plus their bought
# time covers every wall.

class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)
        INF = float("inf")
        dp = [INF] * (n + 1)
        dp[0] = 0
        for c, t in zip(cost, time):
            for k in range(n, -1, -1):
                if dp[k] == INF:
                    continue
                nk = min(n, k + 1 + t)
                if dp[k] + c < dp[nk]:
                    dp[nk] = dp[k] + c
        return dp[n]
