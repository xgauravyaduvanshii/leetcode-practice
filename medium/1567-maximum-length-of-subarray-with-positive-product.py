# LeetCode 1567. Maximum Length of Subarray With Positive Product — Medium
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
# Submission 2199878235 — Accepted, Python3
#
# My thinking: a zero splits the array into
# independent segments. Inside a segment, an
# even count of negatives means the whole
# segment works; with an odd count I cut off
# one end up to the nearest negative.

from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        first_negative = -1
        last_negative = -1
        negatives = 0
        best = 0
        start = 0
        for i, value in enumerate(nums):
            if value == 0:
                first_negative = -1
                negatives = 0
                start = i + 1
            else:
                if value < 0:
                    negatives += 1
                    if first_negative == -1:
                        first_negative = i
                    last_negative = i
                if negatives % 2 == 0:
                    best = max(best, i - start + 1)
                else:
                    best = max(best, i - first_negative, last_negative - start)
        return best
