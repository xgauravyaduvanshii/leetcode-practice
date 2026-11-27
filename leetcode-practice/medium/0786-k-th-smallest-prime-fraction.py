# LeetCode 786. K-th Smallest Prime Fraction — Medium
# https://leetcode.com/problems/k-th-smallest-prime-fraction/
# Submission 2198937199 — Accepted, Python3
#
# My thinking: the array is small enough to list
# every fraction numerator-over-denominator with
# the numerator's index below the denominator's.
# Sorting them gives the k-th smallest directly.

from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fractions.append((arr[i] / arr[j], arr[i], arr[j]))
        fractions.sort()
        _, numerator, denominator = fractions[k - 1]
        return [numerator, denominator]
