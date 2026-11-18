# LeetCode 2913. Subarrays Distinct Element Sum of Squares I — Easy
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
# Submission 2198695559 — Accepted, Python3
#
# My thinking: the input is small, so I expand every
# subarray from its left end, keeping the set of
# distinct numbers so far. Each step adds the square
# of how many distinct numbers the current subarray
# has.

from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for start in range(n):
            distinct = set()
            for end in range(start, n):
                distinct.add(nums[end])
                total += len(distinct) ** 2
        return total
