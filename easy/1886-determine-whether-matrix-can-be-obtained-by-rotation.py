# LeetCode 1886. Determine Whether Matrix Can Be Obtained By Rotation — Easy
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
# Submission 2197603018 — Accepted, Python3
#
# My thinking: a matrix rotated four times comes
# back to itself, so there are only four shapes to
# try. I rotate the matrix 90 degrees at a time —
# transpose then reverse the rows — and check
# whether it ever equals the target.

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        def rotate(m):
            return [list(row) for row in zip(*m[::-1])]
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False
