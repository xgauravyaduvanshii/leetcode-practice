# LeetCode 1738. Find Kth Largest XOR Coordinate Value — Medium
# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
# Submission 2199923214 — Accepted, Python3
#
# My thinking: the xor of the rectangle ending
# at each cell comes from the cells above and
# to the left, cancelling the overlap. I
# collect every cell's value and take the
# k-th largest.

from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        values = []
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = matrix[i][j] ^ prefix[i][j + 1] ^ prefix[i + 1][j] ^ prefix[i][j]
                values.append(prefix[i + 1][j + 1])
        values.sort(reverse=True)
        return values[k - 1]
