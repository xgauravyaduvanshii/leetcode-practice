# LeetCode 794. Valid Tic-Tac-Toe State — Medium
# https://leetcode.com/problems/valid-tic-tac-toe-state/
# Submission 2198941541 — Accepted, Python3
#
# My thinking: X always goes first, so the
# counts can differ by at most one. A win must
# match the counts too — X wins only when it has
# one more move, O wins only when the counts are
# equal — and both cannot win at once.

from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)
        if o_count > x_count or x_count - o_count > 1:
            return False

        def wins(player):
            lines = [board[0], board[1], board[2]]
            lines += ["".join(board[r][c] for r in range(3)) for c in range(3)]
            lines += ["".join(board[i][i] for i in range(3)), "".join(board[i][2 - i] for i in range(3))]
            return player * 3 in lines

        x_wins, o_wins = wins("X"), wins("O")
        if x_wins and o_wins:
            return False
        if x_wins and x_count != o_count + 1:
            return False
        if o_wins and x_count != o_count:
            return False
        return True
