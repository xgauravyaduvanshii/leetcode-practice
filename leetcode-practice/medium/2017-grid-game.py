# LeetCode 2017. Grid Game — Medium
# https://leetcode.com/problems/grid-game/
# Submission 2204143253 — Accepted, Python3
#
# My thinking: the first robot must walk from the top-left corner to the
# bottom-right corner, moving only right or down, so it goes right along the
# top row for a while, drops down at some column i, then goes right along the
# bottom row. Every cell it steps on is emptied, so the second robot, taking
# the same kind of path, can only score from the cells the first robot did
# not touch: the top-row cells after column i, or the bottom-row cells before
# column i. It takes the better of those two, so for a given drop column i
# its score is max(top suffix after i, bottom prefix before i). The first
# robot picks the drop column that makes that best score as small as
# possible, so I try every column and keep the smallest of those maxima.

class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        # Points left in the top row after the drop column: starts as the
        # whole top row except column 0 and shrinks as i moves right.
        top_suffix = sum(grid[0][1:])
        # Points left in the bottom row before the drop column: starts at 0
        # and grows as i moves right.
        bottom_prefix = 0
        ans = float("inf")
        for i in range(n):
            ans = min(ans, max(top_suffix, bottom_prefix))
            # Moving the drop one column right: column i + 1 leaves the top
            # suffix, and column i joins the bottom prefix.
            top_suffix -= grid[0][i + 1] if i + 1 < n else 0
            bottom_prefix += grid[1][i]
        return ans
