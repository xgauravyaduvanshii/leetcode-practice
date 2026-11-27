# LeetCode 200. Number of Islands — Medium
# https://leetcode.com/problems/number-of-islands/
# Submission 2198445330 — Accepted, Python3
#
# My thinking: every unvisited land cell starts a
# new island. I flood-fill from it in all four
# directions, turning its land to water as I go so
# the same island is never counted twice. The
# number of times I start a fill is the answer.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def sink(i: int, j: int) -> None:
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == "1"):
                return
            grid[i][j] = "0"
            sink(i + 1, j)
            sink(i - 1, j)
            sink(i, j + 1)
            sink(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    sink(i, j)
        return count
