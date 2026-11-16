# LeetCode 1030. Matrix Cells in Distance Order — Easy
# https://leetcode.com/problems/matrix-cells-in-distance-order/
# Submission 2197552652 — Accepted, Python3
#
# My thinking: I list every cell in the grid, then
# sort them by Manhattan distance from the centre
# cell — how far across plus how far down. The
# centre itself comes first with distance zero.

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        cells = [[r, c] for r in range(rows) for c in range(cols)]
        cells.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))
        return cells
