# LeetCode 566. Reshape the Matrix — Easy
# https://leetcode.com/problems/reshape-the-matrix/
# Submission 2197498786 — Accepted, Python3
#
# My thinking: if the total number of cells does not
# match, reshaping is impossible and I return the
# original matrix. Otherwise I flatten everything
# into one list in order, then cut it into new rows
# of the right width.

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = [num for row in mat for num in row]
        return [flat[i * c:(i + 1) * c] for i in range(r)]
