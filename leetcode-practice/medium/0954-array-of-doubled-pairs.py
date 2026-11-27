# LeetCode 954. Array of Doubled Pairs — Medium
# https://leetcode.com/problems/array-of-doubled-pairs/
# Submission 2198976075 — Accepted, Python3
#
# My thinking: I pair the smallest values first,
# by size — every number needs its double to
# still be there. Zero pairs with itself, and
# negatives pair with their doubles too, so
# sorting by absolute value handles them all.

from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        for x in sorted(counts, key=abs):
            if counts[x] == 0:
                continue
            if counts[2 * x] < counts[x]:
                return False
            counts[2 * x] -= counts[x]
        return True
