# LeetCode 1496. Path Crossing — Easy
# https://leetcode.com/problems/path-crossing/
# Submission 2197582421 — Accepted, Python3
#
# My thinking: I walk the path step by step from
# (0, 0), remembering every point I have visited.
# If I ever step onto a point I have already been
# to, the path crosses itself.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = {(0, 0)}
        for ch in path:
            if ch == "N":
                y += 1
            elif ch == "S":
                y -= 1
            elif ch == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
