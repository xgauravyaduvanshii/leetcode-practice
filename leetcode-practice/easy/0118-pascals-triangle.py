# LeetCode 118. Pascal's Triangle — Easy
# https://leetcode.com/problems/pascals-triangle/
# Submission 2197441852 — Accepted, Python3
#
# My thinking: every row starts and ends with 1, and
# each number in the middle is the sum of the two
# numbers above it. So I build the triangle row by
# row, using the previous row I just made.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            previous = triangle[-1]
            row = [1]
            for j in range(1, i):
                row.append(previous[j - 1] + previous[j])
            row.append(1)
            triangle.append(row)
        return triangle
