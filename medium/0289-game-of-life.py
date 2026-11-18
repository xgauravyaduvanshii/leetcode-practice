# LeetCode 289. Game of Life — Medium
# https://leetcode.com/problems/game-of-life/
# Submission 2198734497 — Accepted, Python3
#
# My thinking: every cell changes at the same time,
# so I cannot overwrite the board as I go. I mark
# the changes in place instead — 2 for a cell that
# dies, 3 for one that comes alive — and count live
# neighbours by treating 1 and 2 as alive. A final
# pass turns 2 into 0 and 3 into 1.

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                live = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and board[nr][nc] in (1, 2)
                        ):
                            live += 1
                if board[r][c] == 1 and live not in (2, 3):
                    board[r][c] = 2
                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 3
        for r in range(rows):
            for c in range(cols):
                board[r][c] %= 2
