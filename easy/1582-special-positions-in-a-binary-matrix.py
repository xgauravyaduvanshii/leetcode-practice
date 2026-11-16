# LeetCode 1582. Special Positions in a Binary Matrix — Easy
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/
# Submission 2197587742 — Accepted, Python3
#
# My thinking: a position is special when it holds a
# 1 and is the only 1 in both its row and its
# column. I count the ones in each row and column
# first, then check every 1 against those counts.

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows = [sum(row) for row in mat]
        cols = [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1
        return count
