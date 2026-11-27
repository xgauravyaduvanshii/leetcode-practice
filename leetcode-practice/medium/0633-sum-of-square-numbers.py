# LeetCode 633. Sum of Square Numbers — Medium
# https://leetcode.com/problems/sum-of-square-numbers/
# Submission 2198888055 — Accepted, Python3
#
# My thinking: I try every possible first square
# and check whether what is left is a perfect
# square too. The integer square root settles that
# without any floating-point guessing.

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = c - a * a
            root = math.isqrt(b)
            if root * root == b:
                return True
            a += 1
        return False
