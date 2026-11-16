# LeetCode 1351. Count Negative Numbers in a Sorted Matrix — Easy
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Submission 2197572202 — Accepted, Python3
#
# My thinking: the matrix is small enough that I can
# simply look at every value and count the ones
# below zero. Straightforward and correct.

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for row in grid:
            for value in row:
                if value < 0:
                    count += 1
        return count
