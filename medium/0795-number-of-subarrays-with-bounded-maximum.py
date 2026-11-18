# LeetCode 795. Number of Subarrays with Bounded Maximum — Medium
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# Submission 2198941867 — Accepted, Python3
#
# My thinking: subarrays whose maximum is at most
# right, minus those whose maximum is below left,
# leave exactly the ones whose maximum sits in
# range. Each count is just runs of numbers under
# the bound.

from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            total = 0
            run = 0
            for num in nums:
                run = run + 1 if num <= bound else 0
                total += run
            return total

        return count(right) - count(left - 1)
