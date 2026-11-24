# LeetCode 3530. Maximum Profit from Valid Topological Order in DAG — Hard
# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/
# Submission 2202803850 — Accepted, Python3
from typing import List


class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # My thinking: n is at most 22, so I enumerate which nodes
        # have been placed as a bitmask. dp[mask] is the best profit
        # for placing exactly those nodes in the first popcount(mask)
        # positions; from a mask I may place any node whose
        # prerequisites are all already placed, and it earns
        # score[v] times its (1-based) position. The best order is
        # dp over the full mask.
        pre = [0] * n
        for u, v in edges:
            pre[v] |= 1 << u
        N = 1 << n
        NEG = -10 ** 18
        dp = [NEG] * N
        dp[0] = 0
        pop = [0] * N
        for m in range(1, N):
            pop[m] = pop[m >> 1] + (m & 1)
        for mask in range(N):
            if dp[mask] == NEG:
                continue
            pos = pop[mask] + 1
            for v in range(n):
                if mask & (1 << v):
                    continue
                if mask & pre[v] != pre[v]:
                    continue
                nmask = mask | (1 << v)
                val = dp[mask] + score[v] * pos
                if val > dp[nmask]:
                    dp[nmask] = val
        return dp[N - 1]
