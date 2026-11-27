# LeetCode 1300. Sum of Mutated Array Closest to Target — Medium
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
# Submission 2199027324 — Accepted, Python3
#
# My thinking: with the array sorted, capping
# everything above some value changes the sum
# in a predictable way. I find where the cap
# has to fall, then pick the cap value closest
# to the target — the smaller one on a tie.

from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        prefix = 0
        for i, value in enumerate(arr):
            remaining = len(arr) - i
            if value * remaining + prefix >= target:
                best = max(0, (target - prefix) // remaining)
                if abs(prefix + best * remaining - target) <= abs(prefix + (best + 1) * remaining - target):
                    return best
                return best + 1
            prefix += value
        return arr[-1]
