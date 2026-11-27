# LeetCode 3562. Maximum Profit from Trading Stocks with Discounts — Hard
# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/
# Submission 2202847531 — Accepted, Python3
from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # My thinking: a tree knapsack. For each employee I keep two
        # tables over the budget: one for when their boss bought
        # (so their own price is halved) and one for when the boss
        # did not. Whether the employee buys or not, the children
        # only care about that choice — not about the boss — so both
        # tables share the same "employee does not buy" case (the
        # children see no discount) and differ only in the price the
        # employee pays when they do buy.
        children = defaultdict(list)
        for u, v in hierarchy:
            children[u].append(v)
        NEG = -10 ** 9

        def merge(a, b):
            res = [NEG] * (budget + 1)
            for x in range(budget + 1):
                if a[x] == NEG:
                    continue
                for y in range(budget + 1 - x):
                    if b[y] == NEG:
                        continue
                    if a[x] + b[y] > res[x + y]:
                        res[x + y] = a[x] + b[y]
            best = NEG
            for i in range(budget + 1):
                best = max(best, res[i])
                res[i] = best
            return res

        def solve(u):
            comb0 = [0] * (budget + 1)
            comb1 = [0] * (budget + 1)
            for v in children[u]:
                d0, d1 = solve(v)
                comb0 = merge(comb0, d0)
                comb1 = merge(comb1, d1)
            dp0 = comb0[:]
            dp1 = comb0[:]
            c0 = present[u - 1]
            if c0 <= budget:
                profit = future[u - 1] - c0
                for b in range(c0, budget + 1):
                    dp0[b] = max(dp0[b], profit + comb1[b - c0])
            c1 = present[u - 1] // 2
            if c1 <= budget:
                profit = future[u - 1] - c1
                for b in range(c1, budget + 1):
                    dp1[b] = max(dp1[b], profit + comb1[b - c1])
            return dp0, dp1

        dp0, _ = solve(1)
        return max(dp0)
