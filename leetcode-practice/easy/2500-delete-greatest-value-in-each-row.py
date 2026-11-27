# LeetCode 2500. Delete Greatest Value in Each Row — Easy
# https://leetcode.com/problems/delete-greatest-value-in-each-row/
# Submission 2197794406 — Accepted, Python3
#
# My thinking: sorting each row lines up the values
# so that each round deletes the same column — the
# biggest remaining value in each row. I add up the
# biggest value of each column.

class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for row in grid:
            row.sort()
        total = 0
        for col in range(len(grid[0])):
            total += max(row[col] for row in grid)
        return total
