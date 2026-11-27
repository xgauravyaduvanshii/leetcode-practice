# LeetCode 463. Island Perimeter — Easy
# https://leetcode.com/problems/island-perimeter/
# Submission 2197480287 — Accepted, Python3
#
# My thinking: every land cell starts with 4 edges.
# For each neighbour above or to the left that is
# also land, the two cells share an edge — so I
# subtract 2. Checking only up and left is enough,
# because every shared edge gets counted once.

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
        return perimeter
