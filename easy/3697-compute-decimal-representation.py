# 3697. Compute Decimal Representation (Easy)
# https://leetcode.com/problems/compute-decimal-representation/
# Submission 2200044638 — Accepted, Python3
from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        # My thinking: read the number digit by digit
        # from the left. Every non-zero digit becomes
        # its place value — the digit times its power
        # of ten — and zeroes contribute nothing.
        parts = []
        power = 10 ** (len(str(n)) - 1)
        for d in str(n):
            if d != "0":
                parts.append(int(d) * power)
            power //= 10
        return parts
