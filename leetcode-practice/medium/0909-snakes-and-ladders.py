# LeetCode 909. Snakes and Ladders — Medium
# https://leetcode.com/problems/snakes-and-ladders/
# Submission 2198966561 — Accepted, Python3
#
# My thinking: I flatten the board into cell
# numbers first — the rows zigzag — then search
# breadth-first, one dice throw at a time. The
# first time I reach the last cell, that is the
# fewest moves possible.

from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [0]
        flip = False
        for row in reversed(board):
            cells += row if not flip else row[::-1]
            flip = not flip
        queue = deque([(1, 0)])
        seen = {1}
        while queue:
            cell, moves = queue.popleft()
            for step in range(1, 7):
                nxt = cell + step
                if nxt > n * n:
                    continue
                dest = cells[nxt] if cells[nxt] != -1 else nxt
                if dest == n * n:
                    return moves + 1
                if dest not in seen:
                    seen.add(dest)
                    queue.append((dest, moves + 1))
        return -1
