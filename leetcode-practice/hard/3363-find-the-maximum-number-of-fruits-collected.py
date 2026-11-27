# LeetCode 3363. Find the Maximum Number of Fruits Collected — Hard
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/
# Submission 2202425463 — Accepted, Python3
from typing import List

NEG = -10 ** 18


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # My thinking: the child from (0,0) must move diagonally every time
        # to reach (n-1,n-1) in n-1 moves, so it takes the whole main
        # diagonal. The child from (0,n-1) can never go below the diagonal
        # (once below, its column can never catch up to its row in time to
        # reach (n-1,n-1)), and the child from (n-1,0) can never go above
        # it, so the two collect from disjoint regions except the diagonal,
        # which is already taken. I run a DP for each of them with diagonal
        # cells worth zero.
        n = len(fruits)
        diag = sum(fruits[i][i] for i in range(n))
        # child 2: from (0, n-1), moves (1,-1), (1,0), (1,1); region i <= j
        dp = [[NEG] * n for _ in range(n)]
        dp[0][n - 1] = fruits[0][n - 1]
        for i in range(1, n):
            for j in range(i, n):
                best = NEG
                for pj in (j - 1, j, j + 1):
                    if 0 <= pj < n and dp[i - 1][pj] != NEG:
                        best = max(best, dp[i - 1][pj])
                if best != NEG:
                    dp[i][j] = best + (0 if i == j else fruits[i][j])
        child2 = dp[n - 1][n - 1]
        # child 3: from (n-1, 0), moves (-1,1), (0,1), (1,1); region i >= j
        dp = [[NEG] * n for _ in range(n)]
        dp[n - 1][0] = fruits[n - 1][0]
        for j in range(1, n):
            for i in range(j, n):
                best = NEG
                for pi in (i - 1, i, i + 1):
                    if 0 <= pi < n and dp[pi][j - 1] != NEG:
                        best = max(best, dp[pi][j - 1])
                if best != NEG:
                    dp[i][j] = best + (0 if i == j else fruits[i][j])
        child3 = dp[n - 1][n - 1]
        return diag + child2 + child3
