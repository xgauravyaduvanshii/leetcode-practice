# LeetCode 3235. Check if the Rectangle Corner Is Reachable — Hard
# https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/
# Submission 2202115526 — Accepted, Python3
#
# My thinking: the corner is unreachable
# exactly when the circles chain together
# into a barrier across the rectangle —
# left to right, left to bottom, right to
# top, or top to bottom. I union circles
# with the four edges, but two circles
# only union when their lens actually
# meets the rectangle, which I check with
# their intersection points, centres,
# corners and edge crossings.

from typing import List


class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        import math
        X, Y = xCorner, yCorner
        n = len(circles)
        parent = list(range(n + 4))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        def clamp(v, lo, hi):
            return lo if v < lo else hi if v > hi else v

        def lens_in_rect(x1, y1, r1, x2, y2, r2):
            dx = x2 - x1
            dy = y2 - y1
            d2 = dx * dx + dy * dy
            if d2 == 0:
                if r1 <= r2:
                    cx, cy, rr = x1, y1, r1
                else:
                    cx, cy, rr = x2, y2, r2
                clx = clamp(cx, 0, X)
                cly = clamp(cy, 0, Y)
                return (cx - clx) * (cx - clx) + (cy - cly) * (cy - cly) <= rr * rr
            if 0 <= x1 <= X and 0 <= y1 <= Y and (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= r2 * r2:
                return True
            if 0 <= x2 <= X and 0 <= y2 <= Y and (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= r1 * r1:
                return True
            for cx, cy in ((0, 0), (X, 0), (0, Y), (X, Y)):
                if (cx - x1) * (cx - x1) + (cy - y1) * (cy - y1) <= r1 * r1 and (cx - x2) * (cx - x2) + (cy - y2) * (cy - y2) <= r2 * r2:
                    return True
            d = math.sqrt(d2)
            a = (r1 * r1 - r2 * r2 + d2) / (2.0 * d)
            h2 = r1 * r1 - a * a
            if h2 >= 0:
                h = math.sqrt(h2)
                xm = x1 + a * dx / d
                ym = y1 + a * dy / d
                rx = -dy * h / d
                ry = dx * h / d
                for px, py in ((xm + rx, ym + ry), (xm - rx, ym - ry)):
                    if -1e-7 <= px <= X + 1e-7 and -1e-7 <= py <= Y + 1e-7:
                        return True
            for cx, cy, rr, ox, oy, orr in ((x1, y1, r1, x2, y2, r2), (x2, y2, r2, x1, y1, r1)):
                if abs(cx) <= rr:
                    dd = math.sqrt(max(0.0, rr * rr - cx * cx))
                    for py in (cy - dd, cy + dd):
                        if 0 <= py <= Y and math.hypot(0 - ox, py - oy) <= orr + 1e-7:
                            return True
                if abs(cx - X) <= rr:
                    dd = math.sqrt(max(0.0, rr * rr - (cx - X) * (cx - X)))
                    for py in (cy - dd, cy + dd):
                        if 0 <= py <= Y and math.hypot(X - ox, py - oy) <= orr + 1e-7:
                            return True
                if abs(cy) <= rr:
                    dd = math.sqrt(max(0.0, rr * rr - cy * cy))
                    for px in (cx - dd, cx + dd):
                        if 0 <= px <= X and math.hypot(px - ox, 0 - oy) <= orr + 1e-7:
                            return True
                if abs(cy - Y) <= rr:
                    dd = math.sqrt(max(0.0, rr * rr - (cy - Y) * (cy - Y)))
                    for px in (cx - dd, cx + dd):
                        if 0 <= px <= X and math.hypot(px - ox, Y - oy) <= orr + 1e-7:
                            return True
            return False

        TOP, RIGHT, BOTTOM, LEFT = n, n + 1, n + 2, n + 3
        for i, (x, y, r) in enumerate(circles):
            r2 = r * r
            cy = clamp(y, 0, Y)
            if x * x + (y - cy) * (y - cy) <= r2:
                union(i, LEFT)
            if (x - X) * (x - X) + (y - cy) * (y - cy) <= r2:
                union(i, RIGHT)
            cx = clamp(x, 0, X)
            if (x - cx) * (x - cx) + y * y <= r2:
                union(i, BOTTOM)
            if (x - cx) * (x - cx) + (y - Y) * (y - Y) <= r2:
                union(i, TOP)
            for j in range(i):
                x2, y2, r2c = circles[j]
                if (x - x2) * (x - x2) + (y - y2) * (y - y2) <= (r + r2c) * (r + r2c):
                    if lens_in_rect(x, y, r, x2, y2, r2c):
                        union(i, j)
        if find(LEFT) == find(RIGHT):
            return False
        if find(LEFT) == find(BOTTOM):
            return False
        if find(RIGHT) == find(TOP):
            return False
        if find(TOP) == find(BOTTOM):
            return False
        return True
