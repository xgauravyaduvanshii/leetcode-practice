# LeetCode 447. Number of Boomerangs — Medium
# https://leetcode.com/problems/number-of-boomerangs/
# Submission 2198797728 — Accepted, Python3
#
# My thinking: for each point I count how many
# other points sit at each distance from it. Any
# two points at the same distance make a boomerang
# with it in the middle, in either order — that is
# count times count minus one.

from collections import Counter
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for x1, y1 in points:
            distances = Counter(
                (x1 - x2) ** 2 + (y1 - y2) ** 2 for x2, y2 in points
            )
            for count in distances.values():
                total += count * (count - 1)
        return total
