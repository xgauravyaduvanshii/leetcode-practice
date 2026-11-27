# LeetCode 2249. Count Lattice Points Inside a Circle — Medium
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/
# Submission 2204516270 — Accepted, Python3
#
# My thinking: for each circle I walk the horizontal offsets within its
# radius and work out, with an integer square root, how far up and down
# the circle reaches at that offset. Every lattice point I find goes
# into a set so points covered by several circles are counted once, and
# the set size is the answer.
class Solution:
    def countLatticePoints(self, circles: list[list[int]]) -> int:
        import math
        points = set()
        for cx, cy, r in circles:
            r2 = r * r
            for dx in range(-r, r + 1):
                dy = math.isqrt(r2 - dx * dx)
                for y in range(cy - dy, cy + dy + 1):
                    points.add((cx + dx, y))
        return len(points)
