# LeetCode 1711. Count Good Meals — Medium
# https://leetcode.com/problems/count-good-meals/
# Submission 2199916216 — Accepted, Python3
#
# My thinking: a good meal is two dishes whose
# values add to a power of two. I count the
# values, then for each value try every power
# of two and pair it with its complement once.

from collections import Counter
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10 ** 9 + 7
        counts = Counter(deliciousness)
        powers = [1 << i for i in range(22)]
        pairs = 0
        for value in list(counts):
            for power in powers:
                need = power - value
                if need not in counts:
                    continue
                if value == need:
                    pairs += counts[value] * (counts[value] - 1) // 2
                elif value < need:
                    pairs += counts[value] * counts[need]
        return pairs % mod
