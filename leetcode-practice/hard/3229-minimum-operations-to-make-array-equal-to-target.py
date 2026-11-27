# LeetCode 3229. Minimum Operations to Make Array Equal to Target — Hard
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/
# Submission 2202107734 — Accepted, Python3
#
# My thinking: for the differences
# d = target - nums, one operation fixes
# a whole run of the same sign: it costs
# the first |d| in the run plus every
# later increase of |d| inside it. Sign
# changes and zeros start a new run, so I
# just walk the array tracking the
# previous difference.

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        total = 0
        prev = 0
        for a, b in zip(nums, target):
            d = b - a
            if d > 0:
                if prev > 0:
                    if d > prev:
                        total += d - prev
                else:
                    total += d
            elif d < 0:
                if prev < 0:
                    if d < prev:
                        total += prev - d
                else:
                    total += -d
            prev = d
        return total
