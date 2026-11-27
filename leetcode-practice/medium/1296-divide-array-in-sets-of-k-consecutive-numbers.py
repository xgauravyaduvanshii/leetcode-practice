# LeetCode 1296. Divide Array in Sets of K Consecutive Numbers — Medium
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# Submission 2199026593 — Accepted, Python3
#
# My thinking: I work through the numbers in
# order. Whatever is left of the smallest
# number must start that many groups, so I take
# one from each of the next k numbers — if any
# runs out, the split is impossible.

from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counts = Counter(nums)
        for value in sorted(counts):
            need = counts[value]
            if need == 0:
                continue
            for step in range(k):
                if counts[value + step] < need:
                    return False
                counts[value + step] -= need
        return True
