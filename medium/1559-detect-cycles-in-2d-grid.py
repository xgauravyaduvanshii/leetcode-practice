# LeetCode 1559. Detect Cycles in 2D Grid — Medium
# https://leetcode.com/problems/detect-cycles-in-2d-grid/
# Submission 2199876468 — Accepted, Python3
#
# My thinking: a cycle is a same-letter path
# that comes back to a cell it already visited
# without backtracking. I walk each component
# depth-first and flag any visited neighbor
# that is not the cell I just came from.

from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        seen = [[False] * cols for _ in range(rows)]

        def dfs(r, c, pr, pc):
            seen[r][c] = True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c]:
                    if (nr, nc) == (pr, pc):
                        continue
                    if seen[nr][nc]:
                        return True
                    if dfs(nr, nc, r, c):
                        return True
            return False

        for r in range(rows):
            for c in range(cols):
                if not seen[r][c] and dfs(r, c, -1, -1):
                    return True
        return False
