# LeetCode 1905. Count Sub Islands — Medium
# https://leetcode.com/problems/count-sub-islands/
# Submission 2201228311 — Accepted, Python3
#
# My thinking: an island of the second grid
# counts only when every one of its cells is
# also land in the first grid, so I flood-fill
# each island and check that as I go.

class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0
            ok = grid1[i][j] == 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ok = dfs(i + di, j + dj) and ok
            return ok

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    ans += 1
        return ans
