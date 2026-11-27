# LeetCode 598. Range Addition II — Easy
# https://leetcode.com/problems/range-addition-ii/
# Submission 2197503282 — Accepted, Python3
#
# My thinking: every operation adds 1 to a rectangle
# starting at the top-left corner. The cells that
# get every operation are exactly the overlap of
# all those rectangles — a rectangle whose height
# is the smallest row count and whose width is the
# smallest column count.

class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min_row = m
        min_col = n
        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)
        return min_row * min_col
