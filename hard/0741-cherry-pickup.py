# LeetCode 741. Cherry Pickup — Hard
# https://leetcode.com/problems/cherry-pickup/
# Submission 2198670740 — Accepted, Python3
#
# My thinking: going there and coming back is the same
# as two people walking down together from the start.
# Both take the same number of steps, so one walker's
# column follows from the other's position. At each
# step I add the cherries under both walkers — counted
# once if they share a cell — and take the best of the
# four ways to move on.

from functools import lru_cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def best(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return float("-inf")
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            cherries = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]
            next_best = max(
                best(r1 + 1, c1, r2 + 1),
                best(r1 + 1, c1, r2),
                best(r1, c1 + 1, r2 + 1),
                best(r1, c1 + 1, r2),
            )
            return cherries + next_best

        result = best(0, 0, 0)
        return max(result, 0)
