# LeetCode 1900. The Earliest and Latest Rounds Where Players Compete — Hard
# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/
# Submission 2201223134 — Accepted, Python3
#
# My thinking: after every round the winners line
# up again by their original numbers, so a round
# is fully described by how many survivors sit
# below, between and above the two stars — they
# meet when the two side counts are equal, and
# every match between other players can swing
# either way, which is what makes the earliest
# and latest rounds differ.

from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @lru_cache(None)
        def solve(l, m, r):
            if l == r:
                return (1, 1)
            k = l + m + r + 2

            def group(pos):
                if pos <= l:
                    return 'L'
                if pos == l + 1:
                    return 'F'
                if pos <= l + m + 1:
                    return 'M'
                if pos == l + m + 2:
                    return 'S'
                return 'R'

            c = {('L', 'L'): 0, ('M', 'M'): 0, ('R', 'R'): 0,
                 ('L', 'M'): 0, ('L', 'R'): 0, ('M', 'R'): 0}
            mid = None
            for j in range(1, k // 2 + 1):
                g1, g2 = group(j), group(k + 1 - j)
                if 'F' in (g1, g2) or 'S' in (g1, g2):
                    continue
                a, b = sorted((g1, g2))
                c[(a, b)] += 1
            if k % 2 == 1:
                mid = group((k + 1) // 2)
            earliest, latest = 10 ** 9, 0
            for x_lm in range(c[('L', 'M')] + 1):
                for x_lr in range(c[('L', 'R')] + 1):
                    for x_mr in range(c[('M', 'R')] + 1):
                        nl = c[('L', 'L')] + x_lm + x_lr + (1 if mid == 'L' else 0)
                        nm = c[('M', 'M')] + (c[('L', 'M')] - x_lm) + x_mr + (1 if mid == 'M' else 0)
                        nr = c[('R', 'R')] + (c[('L', 'R')] - x_lr) + (c[('M', 'R')] - x_mr) + (1 if mid == 'R' else 0)
                        e, la = solve(nl, nm, nr)
                        earliest = min(earliest, e + 1)
                        latest = max(latest, la + 1)
            return (earliest, latest)

        e, la = solve(firstPlayer - 1, secondPlayer - firstPlayer - 1, n - secondPlayer)
        return [e, la]
