# 3242. Design Neighbor Sum Service (Easy)
# https://leetcode.com/problems/design-neighbor-sum-service/
# Submission 2199989797 — Accepted, Python3
from typing import List


class NeighborSum:
    # My thinking: remember where every value sits in
    # the grid. Then a value's neighbours are just the
    # cells next to its position — straight ones for the
    # adjacent sum, diagonal ones for the diagonal sum.
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.pos = {}
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                self.pos[val] = (r, c)

    def adjacentSum(self, value: int) -> int:
        r, c = self.pos[value]
        total = 0
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                total += self.grid[nr][nc]
        return total

    def diagonalSum(self, value: int) -> int:
        r, c = self.pos[value]
        total = 0
        for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                total += self.grid[nr][nc]
        return total
