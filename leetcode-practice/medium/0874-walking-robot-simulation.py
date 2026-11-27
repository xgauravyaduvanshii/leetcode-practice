# LeetCode 874. Walking Robot Simulation — Medium
# https://leetcode.com/problems/walking-robot-simulation/
# Submission 2198960894 — Accepted, Python3
#
# My thinking: I follow the commands one by one,
# turning left or right and stepping forward
# until an obstacle blocks the way. The farthest
# I ever get from the start is the answer.

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocked = {(x, y) for x, y in obstacles}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        facing = 0
        x = y = 0
        best = 0
        for command in commands:
            if command == -1:
                facing = (facing + 1) % 4
            elif command == -2:
                facing = (facing - 1) % 4
            else:
                dx, dy = directions[facing]
                for _ in range(command):
                    if (x + dx, y + dy) in blocked:
                        break
                    x += dx
                    y += dy
                best = max(best, x * x + y * y)
        return best
