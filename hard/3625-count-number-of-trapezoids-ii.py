# LeetCode 3625. Count Number of Trapezoids II — Hard
# https://leetcode.com/problems/count-number-of-trapezoids-ii/
# Submission 2202887894 — Accepted, Python3
import math
from typing import List
from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # My thinking: two parallel segments on different lines
        # always form a trapezoid, and segments on different lines
        # with the same slope never share an endpoint. So for each
        # slope I group segments by their line and count the pairs
        # drawn from different lines. A parallelogram is counted
        # once per direction, so I count parallelograms separately
        # — two diagonals with the same midpoint, unless they are
        # collinear — and subtract one copy of each.
        n = len(points)
        slope_lines = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                g = math.gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                line = dy * x1 - dx * y1
                slope_lines[(dx, dy)][line] += 1
        total_pairs = 0
        for lines in slope_lines.values():
            total = sum(lines.values())
            total_pairs += total * (total - 1) // 2 - sum(c * (c - 1) // 2 for c in lines.values())
        mid = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                mid[(x1 + x2, y1 + y2)].append((i, j))
        parallelograms = 0
        for pairs in mid.values():
            k = len(pairs)
            if k < 2:
                continue
            slopes = defaultdict(int)
            for (i, j) in pairs:
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = math.gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] += 1
            parallelograms += k * (k - 1) // 2 - sum(c * (c - 1) // 2 for c in slopes.values())
        return total_pairs - parallelograms
