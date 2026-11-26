# LeetCode 1975. Maximum Matrix Sum — Medium
# https://leetcode.com/problems/maximum-matrix-sum/
# Submission 2204083757 — Accepted, Python3
#
# My thinking:
# Flipping any two adjacent cells changes each of their signs. The key
# observation is about the parity of the negative count: one flip changes
# the number of negatives by -2, 0, or +2, so the parity (even or odd)
# of the negative count can never change.
# Because of that, if the matrix starts with an even number of negatives
# we can flip our way to making every entry positive, and the best
# possible sum is simply the sum of all absolute values.
# If the number of negatives is odd, exactly one entry must stay
# negative no matter what we do. To lose as little as possible we leave
# the entry with the smallest absolute value negative, which costs twice
# that value compared with the all-positive sum. A zero in the matrix
# makes this free, since its absolute value is 0.

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negatives = 0
        min_abs = float("inf")

        for row in matrix:
            for value in row:
                total += abs(value)
                if value < 0:
                    negatives += 1
                min_abs = min(min_abs, abs(value))

        if negatives % 2 == 1:
            total -= 2 * min_abs

        return total
