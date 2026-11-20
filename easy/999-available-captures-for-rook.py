# 999. Available Captures for Rook (Easy)
# https://leetcode.com/problems/available-captures-for-rook/
# Submission 2199965558 — Accepted, Python3
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # My thinking: find the rook, then look in each
        # of the four directions. The first piece met in
        # a direction decides it — a pawn counts, a
        # bishop blocks the way, and empty squares just
        # let the look continue.
        rook = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook = (i, j)
        captures = 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            i, j = rook
            while True:
                i += di
                j += dj
                if not (0 <= i < 8 and 0 <= j < 8):
                    break
                if board[i][j] == "p":
                    captures += 1
                    break
                if board[i][j] == "B":
                    break
        return captures
