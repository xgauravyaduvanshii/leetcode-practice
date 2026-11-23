# LeetCode 2732. Find a Good Subset of the Matrix — Hard
# https://leetcode.com/problems/find-a-good-subset-of-the-matrix/
# Submission 2201877768 — Accepted, Python3
#
# My thinking: a single row of all
# zeroes is already good on its own,
# and two rows that never share a 1 are
# good together — and if neither of
# those exists, no larger group can be
# good either, because every row would
# still clash with another.

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: list[list[int]]) -> list[int]:
        masks = []
        for row in grid:
            mask = 0
            for j, v in enumerate(row):
                if v:
                    mask |= 1 << j
            masks.append(mask)
            if mask == 0:
                return [len(masks) - 1]
        m = len(masks)
        for i in range(m):
            for j in range(i + 1, m):
                if masks[i] & masks[j] == 0:
                    return [i, j]
        return []
