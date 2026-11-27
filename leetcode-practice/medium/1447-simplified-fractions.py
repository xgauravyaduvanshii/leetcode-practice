# LeetCode 1447. Simplified Fractions — Medium
# https://leetcode.com/problems/simplified-fractions/
# Submission 2199853121 — Accepted, Python3
#
# My thinking: every fraction with a
# denominator up to n, numerator below it, and
# no common factor is already simplified. I
# list them in order.

from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for den in range(2, n + 1):
            for num in range(1, den):
                if gcd(num, den) == 1:
                    result.append(f"{num}/{den}")
        return result
