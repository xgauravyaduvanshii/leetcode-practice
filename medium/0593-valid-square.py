# LeetCode 593. Valid Square — Medium
# https://leetcode.com/problems/valid-square/
# Submission 2198876562 — Accepted, Python3
#
# My thinking: four points make a square when the
# six distances between them sort into four equal
# sides and two equal diagonals, each diagonal
# twice the side in squared length.

from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        points = [p1, p2, p3, p4]
        distances = sorted(
            distance(points[i], points[j])
            for i in range(4)
            for j in range(i + 1, 4)
        )
        return (
            distances[0] > 0
            and distances[0] == distances[1] == distances[2] == distances[3]
            and distances[4] == distances[5] == 2 * distances[0]
        )
