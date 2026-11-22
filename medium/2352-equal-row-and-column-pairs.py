# LeetCode 2352. Equal Row and Column Pairs — Medium
# https://leetcode.com/problems/equal-row-and-column-pairs/
# Submission 2200967367 — Accepted, Python3
#
# My thinking: I count how many times each row appears,
# then for every column I add the count of rows that
# look exactly like it.

from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)
        return sum(rows[tuple(col)] for col in zip(*grid))
