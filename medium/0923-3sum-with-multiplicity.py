# LeetCode 923. 3Sum With Multiplicity — Medium
# https://leetcode.com/problems/3sum-with-multiplicity/
# Submission 2198970057 — Accepted, Python3
#
# My thinking: I count how many of each value
# there are, then try every triple of values in
# order. The count for a triple depends on
# whether its values repeat — I use the right
# combination formula for each case.

from collections import Counter
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        counts = Counter(arr)
        values = sorted(counts)
        total = 0
        for i, a in enumerate(values):
            for j in range(i, len(values)):
                b = values[j]
                c = target - a - b
                if c < b or c not in counts:
                    continue
                if a == b == c:
                    total += counts[a] * (counts[a] - 1) * (counts[a] - 2) // 6
                elif a == b:
                    total += counts[a] * (counts[a] - 1) // 2 * counts[c]
                elif b == c:
                    total += counts[a] * counts[b] * (counts[b] - 1) // 2
                else:
                    total += counts[a] * counts[b] * counts[c]
        return total % MOD
