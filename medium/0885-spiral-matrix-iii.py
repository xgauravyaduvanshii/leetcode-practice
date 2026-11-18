# LeetCode 885. Spiral Matrix III — Medium
# https://leetcode.com/problems/spiral-matrix-iii/
# Submission 2198962251 — Accepted, Python3
#
# My thinking: I walk in a spiral — right, down,
# left, up — with the legs growing by one every
# two turns. Only the steps inside the grid are
# recorded, until every cell is visited.

from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = [[rStart, cStart]]
        steps = 1
        r, c = rStart, cStart
        while len(result) < rows * cols:
            for dr, dc, length in ((0, 1, steps), (1, 0, steps), (0, -1, steps + 1), (-1, 0, steps + 1)):
                for _ in range(length):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                if len(result) == rows * cols:
                    return result
            steps += 2
        return result
