# LeetCode 858. Mirror Reflection — Medium
# https://leetcode.com/problems/mirror-reflection/
# Submission 2198956709 — Accepted, Python3
#
# My thinking: the ray keeps bouncing until it
# lands on a corner, which happens after a whole
# number of room widths and heights — their least
# common multiple. Whether those counts are odd
# or even says which corner it is.

import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p * q // math.gcd(p, q)
        horizontal = lcm // p
        vertical = lcm // q
        if vertical % 2 == 0:
            return 2
        if horizontal % 2 == 0:
            return 0
        return 1
