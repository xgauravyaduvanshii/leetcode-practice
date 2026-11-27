# LeetCode 1914. Cyclically Rotating a Grid — Medium
# https://leetcode.com/problems/cyclically-rotating-a-grid/
# Submission 2201575522 — Accepted, Python3
#
# My thinking: each ring of the grid turns on
# its own, so I lift every ring out in order,
# shift it by k, and lay it back down exactly
# where it came from.

class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            ring = []
            for c in range(left, right + 1):
                ring.append(grid[top][c])
            for r in range(top + 1, bottom + 1):
                ring.append(grid[r][right])
            for c in range(right - 1, left - 1, -1):
                ring.append(grid[bottom][c])
            for r in range(bottom - 1, top, -1):
                ring.append(grid[r][left])
            shift = k % len(ring)
            ring = ring[shift:] + ring[:shift]
            i = 0
            for c in range(left, right + 1):
                grid[top][c] = ring[i]
                i += 1
            for r in range(top + 1, bottom + 1):
                grid[r][right] = ring[i]
                i += 1
            for c in range(right - 1, left - 1, -1):
                grid[bottom][c] = ring[i]
                i += 1
            for r in range(bottom - 1, top, -1):
                grid[r][left] = ring[i]
                i += 1
        return grid
