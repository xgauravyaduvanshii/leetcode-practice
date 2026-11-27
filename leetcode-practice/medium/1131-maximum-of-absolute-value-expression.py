# LeetCode 1131. Maximum of Absolute Value Expression — Medium
# https://leetcode.com/problems/maximum-of-absolute-value-expression/
# Submission 2199004045 — Accepted, Python3
#
# My thinking: the absolute values unfold into
# eight sign choices. For each choice the
# expression is a plain sum, so the biggest gap
# between its largest and smallest values is
# the answer for that choice.

from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        best = 0
        for sx in (1, -1):
            for sy in (1, -1):
                for sz in (1, -1):
                    highest = float("-inf")
                    lowest = float("inf")
                    for i, (a, b) in enumerate(zip(arr1, arr2)):
                        value = sx * a + sy * b + sz * i
                        highest = max(highest, value)
                        lowest = min(lowest, value)
                    best = max(best, highest - lowest)
        return best
