# LeetCode 1706. Where Will the Ball Fall — Medium
# https://leetcode.com/problems/where-will-the-ball-fall/
# Submission 2199915708 — Accepted, Python3
#
# My thinking: I drop a ball from each column
# and follow it down. A board turns the ball
# aside; it gets stuck when the next board
# points the other way or the edge is there.

from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        result = []
        for start in range(cols):
            col = start
            for row in range(rows):
                direction = grid[row][col]
                next_col = col + direction
                if next_col < 0 or next_col >= cols or grid[row][next_col] != direction:
                    col = -1
                    break
                col = next_col
            result.append(col)
        return result
