# LeetCode 1387. Sort Integers by The Power Value — Medium
# https://leetcode.com/problems/sort-integers-by-the-power-value/
# Submission 2199047136 — Accepted, Python3
#
# My thinking: the power of a number is how
# many Collatz steps it takes to reach one. I
# memoise those counts, then sort the range by
# power — and by the number itself on a tie.

from functools import lru_cache
from typing import List


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(maxsize=None)
        def power(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                return 1 + power(n // 2)
            return 1 + power(3 * n + 1)

        return sorted(range(lo, hi + 1), key=lambda x: (power(x), x))[k - 1]
