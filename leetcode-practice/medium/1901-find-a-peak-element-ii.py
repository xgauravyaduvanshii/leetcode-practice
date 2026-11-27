# LeetCode 1901. Find a Peak Element II — Medium
# https://leetcode.com/problems/find-a-peak-element-ii/
# Submission 2201177627 — Accepted, Python3
#
# My thinking: I binary-search the columns — in
# the middle column I take its tallest cell, and
# if a neighbour is taller I move that way, since
# the tallest cell of the next column can only be
# taller still.

class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            row = max(range(m), key=lambda r: mat[r][mid])
            left = mat[row][mid - 1] if mid > 0 else -1
            right = mat[row][mid + 1] if mid < n - 1 else -1
            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif left > mat[row][mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return [-1, -1]
