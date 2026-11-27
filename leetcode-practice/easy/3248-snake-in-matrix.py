# 3248. Snake in Matrix (Easy)
# https://leetcode.com/problems/snake-in-matrix/
# Submission 2199990167 — Accepted, Python3
from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # My thinking: start in the top-left corner and
        # follow the commands — up, down, left, right —
        # keeping the row and column. The final cell's
        # number is its row times the size plus its
        # column.
        r = 0
        c = 0
        for cmd in commands:
            if cmd == "UP":
                r -= 1
            elif cmd == "DOWN":
                r += 1
            elif cmd == "LEFT":
                c -= 1
            else:
                c += 1
        return r * n + c
