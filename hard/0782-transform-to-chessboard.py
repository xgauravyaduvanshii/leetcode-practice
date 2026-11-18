# LeetCode 782. Transform to Chessboard — Hard
# https://leetcode.com/problems/transform-to-chessboard/
# Submission 2198676143 — Accepted, Python3
#
# My thinking: a chessboard has only two kinds of
# rows — the first row, or its exact opposite — and
# the same for columns, so I check that first. Then
# each line just needs to be made alternating: I count
# the mismatches against the two alternating patterns
# and take the cheaper one that fits the count of
# ones.

from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        first_row = board[0]
        first_col = [board[i][0] for i in range(n)]
        for row in board:
            if row != first_row and row != [1 - x for x in first_row]:
                return -1
        for col in zip(*board):
            if list(col) != first_col and list(col) != [1 - x for x in first_col]:
                return -1

        def swaps(line):
            ones = sum(line)
            if ones not in (n // 2, (n + 1) // 2):
                return -1
            wrong_start0 = sum(1 for i, v in enumerate(line) if v != i % 2)
            wrong_start1 = n - wrong_start0
            if n % 2 == 0:
                return min(wrong_start0, wrong_start1) // 2
            if ones == n // 2:
                return wrong_start0 // 2
            return wrong_start1 // 2

        row_swaps = swaps(first_row)
        col_swaps = swaps(first_col)
        if row_swaps == -1 or col_swaps == -1:
            return -1
        return row_swaps + col_swaps
