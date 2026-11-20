# LeetCode 1828. Queries on Number of Points Inside a Circle — Medium
# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
# Submission 2199944663 — Accepted, Python3
#
# My thinking: a point is inside a circle
# when the squared distance to its centre is
# no bigger than the squared radius. I just
# count that for every query.

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for qx, qy, radius in queries:
            count = 0
            for x, y in points:
                if (x - qx) ** 2 + (y - qy) ** 2 <= radius ** 2:
                    count += 1
            result.append(count)
        return result
