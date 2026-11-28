# LeetCode 2658. Maximum Number of Fish in a Grid — Medium
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
# Submission 2205113197 — Accepted, Python3
#
# My thinking: fish only connect through neighbouring land
# cells, so each connected component of positive cells is one
# catch. Flood-fill every unvisited land cell, total its
# fish, and keep the biggest total.
class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or seen[i][j]:
                    continue
                stack = [(i, j)]
                seen[i][j] = True
                total = 0
                while stack:
                    r, c = stack.pop()
                    total += grid[r][c]
                    for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < m and 0 <= nc < n
                                and not seen[nr][nc] and grid[nr][nc] > 0):
                            seen[nr][nc] = True
                            stack.append((nr, nc))
                ans = max(ans, total)
        return ans
