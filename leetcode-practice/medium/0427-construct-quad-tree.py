# LeetCode 427. Construct Quad Tree — Medium
# https://leetcode.com/problems/construct-quad-tree/
# Submission 2198787993 — Accepted, Python3
#
# My thinking: a square of one value is a leaf. Any
# other square splits into four quarters, and each
# quarter becomes a child built the same way.

class Solution:
    def construct(self, grid: list[list[int]]):
        n = len(grid)

        def build(r, c, size):
            value = grid[r][c]
            same = all(
                grid[i][j] == value
                for i in range(r, r + size)
                for j in range(c, c + size)
            )
            if same:
                return Node(value == 1, True)
            half = size // 2
            return Node(
                True,
                False,
                build(r, c, half),
                build(r, c + half, half),
                build(r + half, c, half),
                build(r + half, c + half, half),
            )

        return build(0, 0, n)
