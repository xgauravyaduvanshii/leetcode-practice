# LeetCode 808. Soup Servings — Medium
# https://leetcode.com/problems/soup-servings/
# Submission 2198943436 — Accepted, Python3
#
# My thinking: the soups only change in 25 ml
# steps, so I scale the amounts down and work out
# the odds with memoised recursion — A finishing
# first, B finishing first, or both together.
# With a huge amount of soup, A almost surely
# finishes first.

from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
        units = (n + 24) // 25

        @lru_cache(maxsize=None)
        def chance(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (chance(a - 4, b) + chance(a - 3, b - 1) + chance(a - 2, b - 2) + chance(a - 1, b - 3))

        return chance(units, units)
