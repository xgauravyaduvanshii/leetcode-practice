# LeetCode 592. Fraction Addition and Subtraction — Medium
# https://leetcode.com/problems/fraction-addition-and-subtraction/
# Submission 2198875932 — Accepted, Python3
#
# My thinking: I pull each fraction out of the
# expression with its sign, add it into a running
# total, and reduce by the greatest common divisor
# after every step so the numbers stay small.

import math
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator, denominator = 0, 1
        for sign, top, bottom in re.findall(r"([+-]?)(\d+)/(\d+)", expression):
            top = int(top) * (-1 if sign == "-" else 1)
            bottom = int(bottom)
            numerator = numerator * bottom + top * denominator
            denominator = denominator * bottom
            common = math.gcd(numerator, denominator)
            numerator //= common
            denominator //= common
        return f"{numerator}/{denominator}"
