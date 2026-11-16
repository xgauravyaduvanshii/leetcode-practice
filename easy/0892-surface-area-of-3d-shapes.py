# LeetCode 892. Surface Area of 3D Shapes — Easy
# https://leetcode.com/problems/surface-area-of-3d-shapes/
# Submission 2197538931 — Accepted, Python3
#
# My thinking: a stack of v cubes on its own has a
# top, a bottom, and 4 sides per cube — 2 + 4v.
# But where two stacks touch, the shared faces are
# hidden. So for each cell I subtract twice the
# height of the overlap with the stack above it
# and the stack to its left (each shared face
# hides one face on each stack).

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v > 0:
                    area += 2 + 4 * v
                    if i > 0:
                        area -= 2 * min(v, grid[i - 1][j])
                    if j > 0:
                        area -= 2 * min(v, grid[i][j - 1])
        return area
