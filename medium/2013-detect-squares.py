# LeetCode 2013. Detect Squares — Medium
# https://leetcode.com/problems/detect-squares/
# Submission 2204138393 — Accepted, Python3

# My thinking:
# I keep a count of every point added so far, keyed by its (x, y) coordinates,
# because the same point can be added more than once and each copy counts.
# To count squares with a query point as one corner, I look for a second point
# straight above or below it on the same x — that gives me the side length of
# a possible square. For a vertical side of length d, the other two corners
# must sit d units to the left or to the right, at the same two y-values.
# So for each point (x, y2) sharing the query point's x, I check both the
# left and right columns: the number of squares through that pair is the
# product of the three point counts — the vertical partner and the two
# corners in the other column. Adding those products up over all vertical
# partners gives the answer. There are at most a few hundred distinct points
# on one column, so this is fast enough.

from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.counts[(point[0], point[1])] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        total = 0
        for (px, py), c in self.counts.items():
            if px != x or py == y:
                continue
            d = abs(py - y)
            # Squares to the right of the vertical side.
            total += c * self.counts.get((x + d, y), 0) * self.counts.get((x + d, py), 0)
            # Squares to the left of the vertical side.
            total += c * self.counts.get((x - d, y), 0) * self.counts.get((x - d, py), 0)
        return total
