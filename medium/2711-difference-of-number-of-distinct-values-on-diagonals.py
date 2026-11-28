# LeetCode 2711. Difference of Number of Distinct Values on Diagonals — Medium
# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/
# Submission 2205203898 — Accepted, Python3
#
# My thinking: for each cell, walk its diagonal up-left and
# down-right collecting the values into two sets (the cell
# itself is excluded on both sides). The answer is the absolute
# difference of the two set sizes. The grid is at most 50x50,
# so walking every diagonal from every cell is cheap.
class Solution:
    def differenceOfDistinctValues(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                up = set()
                i, j = r - 1, c - 1
                while i >= 0 and j >= 0:
                    up.add(grid[i][j])
                    i -= 1
                    j -= 1
                down = set()
                i, j = r + 1, c + 1
                while i < m and j < n:
                    down.add(grid[i][j])
                    i += 1
                    j += 1
                ans[r][c] = abs(len(up) - len(down))
        return ans
