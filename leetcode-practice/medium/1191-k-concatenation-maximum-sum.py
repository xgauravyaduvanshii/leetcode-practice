# LeetCode 1191. K-Concatenation Maximum Sum — Medium
# https://leetcode.com/problems/k-concatenation-maximum-sum/
# Submission 2199009915 — Accepted, Python3
#
# My thinking: the best run lives inside two
# copies of the array. If the whole array sums
# positive, the middle copies add their total
# on top of that; otherwise two copies are
# already the best.

from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        total = sum(arr)

        def kadane(values):
            best = current = 0
            for value in values:
                current = max(0, current + value)
                best = max(best, current)
            return best

        if k == 1:
            return kadane(arr) % mod
        doubled = kadane(arr * 2)
        if total > 0:
            return (doubled + (k - 2) * total) % mod
        return doubled % mod
