# LeetCode 329. Longest Increasing Path in a Matrix — Hard
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Submission 2198406094 — Accepted, Python3
#
# My thinking: from each cell I step to any larger
# neighbour and ask the same question there, keeping
# the longest chain I find. I remember the answer
# for every cell I have already solved, so each cell
# is worked out once. The best chain over all cells
# is the answer.

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if memo[i][j]:
                return memo[i][j]
            best = 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ni, nj))
            memo[i][j] = best
            return best

        return max(dfs(i, j) for i in range(m) for j in range(n))
