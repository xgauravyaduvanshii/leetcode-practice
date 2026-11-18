# LeetCode 51. N-Queens — Hard
# https://leetcode.com/problems/n-queens/
# Submission 2198378836 — Accepted, Python3
#
# My thinking: I place queens row by row. For
# each row I try every column that is not already
# attacked — I keep the used columns and the two
# diagonal directions in sets, so the check is
# instant. When every row has a queen, I save a
# copy of the board; then I take the last queen
# back out and try the next column.

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        cols = set()
        diag_down = set()
        diag_up = set()
        board = [["."] * n for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                boards.append(["".join(line) for line in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag_down or (row + col) in diag_up:
                    continue
                cols.add(col)
                diag_down.add(row - col)
                diag_up.add(row + col)
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."
                cols.remove(col)
                diag_down.remove(row - col)
                diag_up.remove(row + col)

        backtrack(0)
        return boards
