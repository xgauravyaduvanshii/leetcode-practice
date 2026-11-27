# LeetCode 883. Projection Area of 3D Shapes — Easy
# https://leetcode.com/problems/projection-area-of-3d-shapes/
# Submission 2197537580 — Accepted, Python3
#
# My thinking: the total area is three views added
# together. From the top, every non-empty stack
# shows one square. From the front, each row shows
# its tallest stack. From the side, each column
# shows its tallest stack.

class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        top = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        front = sum(max(grid[i]) for i in range(n))
        side = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return top + front + side
