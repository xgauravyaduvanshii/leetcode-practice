# LeetCode 529. Minesweeper — Medium
# https://leetcode.com/problems/minesweeper/
# Submission 2198850472 — Accepted, Python3
#
# My thinking: clicking a mine ends the game on
# that cell. Otherwise I reveal the cell — a digit
# when mines touch it, blank when none do — and a
# blank cell spreads the reveal to its unrevealed
# neighbours.

from collections import deque
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        queue = deque([(r, c)])
        while queue:
            r, c = queue.popleft()
            if board[r][c] != "E":
                continue
            mines = sum(
                board[nr][nc] == "M"
                for nr in range(max(0, r - 1), min(rows, r + 2))
                for nc in range(max(0, c - 1), min(cols, c + 2))
            )
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = "B"
                for nr in range(max(0, r - 1), min(rows, r + 2)):
                    for nc in range(max(0, c - 1), min(cols, c + 2)):
                        if board[nr][nc] == "E":
                            queue.append((nr, nc))
        return board
