# LeetCode 1508. Range Sum of Sorted Subarray Sums — Medium
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
# Submission 2199866071 — Accepted, Python3
#
# My thinking: the array is small enough to
# list every subarray sum, sort them, and add
# up the slice asked for.

from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                sums.append(total)
        sums.sort()
        return sum(sums[left - 1:right]) % (10 ** 9 + 7)
