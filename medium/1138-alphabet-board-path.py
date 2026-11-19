# LeetCode 1138. Alphabet Board Path — Medium
# https://leetcode.com/problems/alphabet-board-path/
# Submission 2199004260 — Accepted, Python3
#
# My thinking: I move from letter to letter on
# the board, always going up and left before
# going down or right — that way I never step
# off the board on the lonely last row, where
# only z lives.

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        moves = []
        row, col = 0, 0
        for ch in target:
            dest_row, dest_col = divmod(ord(ch) - 97, 5)
            while row > dest_row:
                moves.append("U")
                row -= 1
            while col > dest_col:
                moves.append("L")
                col -= 1
            while row < dest_row:
                moves.append("D")
                row += 1
            while col < dest_col:
                moves.append("R")
                col += 1
            moves.append("!")
        return "".join(moves)
