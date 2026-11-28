# LeetCode 2579. Count Total Number of Colored Cells — Medium
# https://leetcode.com/problems/count-total-number-of-colored-cells/
# Submission 2205082316 — Accepted, Python3
#
# My thinking: minute 1 colours 1 cell; each later minute adds
# a ring of 4 more cells than the last (4, 8, 12, ...). The
# total after n minutes is 1 + 4 * (1 + 2 + ... + n-1), which
# is 1 + 2*n*(n-1).
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)
