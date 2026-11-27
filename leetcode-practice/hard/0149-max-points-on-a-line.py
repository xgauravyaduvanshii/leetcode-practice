# LeetCode 149. Max Points on a Line — Hard
# https://leetcode.com/problems/max-points-on-a-line/
# Submission 2198390107 — Accepted, Python3
#
# My thinking: for each point I look at the slope
# to every later point. I reduce each slope to its
# simplest whole-number form and fix its sign, so
# the same line always gives the same pair of
# numbers. The most common slope from that point,
# plus any points sitting exactly on it, is the
# best line through it — and the best over all
# points is the answer.

from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        best = 0
        for i in range(n):
            slopes = {}
            same = 1
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1
            best = max(best, same + (max(slopes.values()) if slopes else 0))
        return best
