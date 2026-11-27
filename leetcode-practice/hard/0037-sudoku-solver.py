# LeetCode 37. Sudoku Solver — Hard
# https://leetcode.com/problems/sudoku-solver/
# Submission 2198364880 — Accepted, Python3
#
# My thinking: I note which digits each row, column
# and 3x3 box already has, and collect the empty
# cells. Then I fill the empty cells one by one,
# trying every digit that does not clash with its
# row, column or box. When a digit leads nowhere,
# I take it back out and try the next one — the
# puzzle has one solution, so the first full board
# I reach is the answer.

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r // 3) * 3 + c // 3].add(board[r][c])

        def backtrack(i: int) -> bool:
            if i == len(empties):
                return True
            r, c = empties[i]
            box = (r // 3) * 3 + c // 3
            for d in "123456789":
                if d not in rows[r] and d not in cols[c] and d not in boxes[box]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[box].add(d)
                    if backtrack(i + 1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[box].remove(d)
            return False

        backtrack(0)
