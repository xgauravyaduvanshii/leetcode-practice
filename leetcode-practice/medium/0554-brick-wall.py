# LeetCode 554. Brick Wall — Medium
# https://leetcode.com/problems/brick-wall/
# Submission 2198862542 — Accepted, Python3
#
# My thinking: a vertical line crosses the fewest
# bricks where the most brick edges already line
# up. I count every edge position and take the
# busiest one.

from collections import Counter
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = Counter()
        for row in wall:
            position = 0
            for brick in row[:-1]:
                position += brick
                edges[position] += 1
        return len(wall) - max(edges.values(), default=0)
