# LeetCode 1338. Reduce Array Size to The Half — Medium
# https://leetcode.com/problems/reduce-array-size-to-the-half/
# Submission 2199033437 — Accepted, Python3
#
# My thinking: removing the most common values
# first shrinks the array fastest. I take
# values in order of frequency until at least
# half the array is gone.

from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequencies = sorted(Counter(arr).values(), reverse=True)
        removed = 0
        for i, count in enumerate(frequencies, 1):
            removed += count
            if removed * 2 >= len(arr):
                return i
        return len(frequencies)
