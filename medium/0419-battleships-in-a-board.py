# LeetCode 419. Battleships in a Board — Medium
# https://leetcode.com/problems/battleships-in-a-board/
# Submission 2198785575 — Accepted, Python3
#
# My thinking: each battleship is a straight line,
# so it has exactly one cell with no X above it and
# no X to its left — its top-left end. I count just
# those cells and never touch the board.

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "X":
                    continue
                if r > 0 and board[r - 1][c] == "X":
                    continue
                if c > 0 and board[r][c - 1] == "X":
                    continue
                count += 1
        return count
