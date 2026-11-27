# LeetCode 2088. Count Fertile Pyramids in a Land — Hard
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
# Submission 2201567887 — Accepted, Python3
#
# My thinking: a pyramid stands on the three
# pyramids below it, so I grow the tallest
# pyramid at every cell from the ones under it
# — once pointing down, once pointing up — and
# every extra level above the first is one more
# pyramid.

class Solution:
    def countPyramids(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # f[i][j]: tallest pyramid with apex at (i, j), widening downward.
        f = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == m - 1 or j == 0 or j == n - 1:
                    f[i][j] = 1
                else:
                    f[i][j] = 1 + min(f[i + 1][j - 1], f[i + 1][j], f[i + 1][j + 1])
                ans += f[i][j] - 1
        # g[i][j]: tallest pyramid with apex at (i, j), widening upward.
        g = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == 0 or j == 0 or j == n - 1:
                    g[i][j] = 1
                else:
                    g[i][j] = 1 + min(g[i - 1][j - 1], g[i - 1][j], g[i - 1][j + 1])
                ans += g[i][j] - 1
        return ans
