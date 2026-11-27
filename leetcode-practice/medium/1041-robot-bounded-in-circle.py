# LeetCode 1041. Robot Bounded In Circle — Medium
# https://leetcode.com/problems/robot-bounded-in-circle/
# Submission 2198992596 — Accepted, Python3
#
# My thinking: I run the instructions once. If
# the robot is back at the start, it stays in a
# loop — and if it ends facing a different
# direction, the loop still closes within four
# rounds. Only a robot that walks away facing
# north escapes.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        direction = 0
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for ch in instructions:
            if ch == "G":
                dx, dy = moves[direction]
                x += dx
                y += dy
            elif ch == "L":
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4
        return (x == 0 and y == 0) or direction != 0
