# LeetCode 365. Water and Jug Problem — Medium
# https://leetcode.com/problems/water-and-jug-problem/
# Submission 2198757644 — Accepted, Python3
#
# My thinking: every amount I can measure is a
# multiple of the greatest common divisor of the two
# jug sizes — that is Bezout's identity. So the
# target works exactly when it fits in both jugs
# together and is a multiple of that divisor.

import math


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        if target == 0:
            return True
        return target % math.gcd(x, y) == 0
