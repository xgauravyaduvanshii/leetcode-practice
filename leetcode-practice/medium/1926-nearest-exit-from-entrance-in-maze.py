# LeetCode 1926. Nearest Exit from Entrance in Maze — Medium
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# Submission 2200982523 — Accepted, Python3
#
# My thinking: I walk outward from the entrance one step
# at a time, and the first border cell I reach that is
# not the entrance is the nearest exit.

from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        while queue:
            r, c, steps = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1
                    maze[nr][nc] = "+"
                    queue.append((nr, nc, steps + 1))
        return -1
