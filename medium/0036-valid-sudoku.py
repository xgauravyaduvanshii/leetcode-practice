# LeetCode 36. Valid Sudoku — Medium
# https://leetcode.com/problems/valid-sudoku/
# Submission 2203817102 — Accepted, Python3
#
# My thinking: I walk every filled cell once and remember which digits
# I have already seen in its row, its column, and its 3x3 box. If a
# digit turns up twice in any of those three groups, the board is
# invalid; if I finish the walk without a repeat, it is valid. The box
# index comes from the row and column divided by 3.

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue
                box = (r // 3) * 3 + c // 3
                if ch in rows[r] or ch in cols[c] or ch in boxes[box]:
                    return False
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box].add(ch)
        return True
