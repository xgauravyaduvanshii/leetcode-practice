# LeetCode 1391. Check if There is a Valid Path in a Grid — Medium
# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
# Submission 2199048033 — Accepted, Python3
#
# My thinking: each street type joins two
# directions, so I walk from the start cell
# and only step into a neighbour when both
# cells open toward each other.

from collections import deque
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        pipes = {
            1: {"left": "right", "right": "left"},
            2: {"up": "down", "down": "up"},
            3: {"left": "down", "down": "left"},
            4: {"right": "down", "down": "right"},
            5: {"left": "up", "up": "left"},
            6: {"right": "up", "up": "right"},
        }
        moves = {"left": (0, -1, "right"), "right": (0, 1, "left"), "up": (-1, 0, "down"), "down": (1, 0, "up")}
        rows = len(grid)
        cols = len(grid[0])
        seen = {(0, 0)}
        queue = deque([(0, 0)])
        while queue:
            r, c = queue.popleft()
            if (r, c) == (rows - 1, cols - 1):
                return True
            for direction, entry in pipes[grid[r][c]].items():
                dr, dc, need = moves[direction]
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and need in pipes[grid[nr][nc]]:
                    seen.add((nr, nc))
                    queue.append((nr, nc))
        return False
