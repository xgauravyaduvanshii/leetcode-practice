# 3483. Unique 3-Digit Even Numbers (Easy)
# https://leetcode.com/problems/unique-3-digit-even-numbers/
# Submission 2200020991 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # My thinking: a valid number has three digits,
        # no leading zero, and an even last digit. I
        # try every even three-digit number and keep
        # the ones I can build from the digits I have.
        counts = Counter(digits)
        total = 0
        for num in range(100, 1000, 2):
            need = Counter(map(int, str(num)))
            if all(counts[d] >= c for d, c in need.items()):
                total += 1
        return total
