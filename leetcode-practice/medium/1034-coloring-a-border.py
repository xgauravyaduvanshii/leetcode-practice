# LeetCode 1034. Coloring A Border — Medium
# https://leetcode.com/problems/coloring-a-border/
# Submission 2198990061 — Accepted, Python3
#
# My thinking: I walk the whole connected region
# of the starting colour. A cell is on the border
# when any neighbour is out of bounds or a
# different colour — only those cells get the new
# colour.

from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        original = grid[row][col]
        stack = [(row, col)]
        seen = {(row, col)}
        border = []
        while stack:
            r, c = stack.pop()
            is_border = False
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != original:
                    is_border = True
                elif (nr, nc) not in seen:
                    seen.add((nr, nc))
                    stack.append((nr, nc))
            if is_border:
                border.append((r, c))
        for r, c in border:
            grid[r][c] = color
        return grid
