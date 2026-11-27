# LeetCode 62. Unique Paths — Medium
# https://leetcode.com/problems/unique-paths/
# Submission 2201006655 — Accepted, Python3
#
# My thinking: every cell's count is the sum of the cell
# above and the cell to the left, so I fill the grid one
# row at a time with just one row of memory.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]
