# LeetCode 1749. Maximum Absolute Sum of Any Subarray — Medium
# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
# Submission 2199927175 — Accepted, Python3
#
# My thinking: the biggest absolute sum is
# either the biggest positive run or the
# biggest negative run. I track both with
# Kadane's rule and keep the larger absolute.

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ending = 0
        min_ending = 0
        best = 0
        for num in nums:
            max_ending = max(num, max_ending + num)
            min_ending = min(num, min_ending + num)
            best = max(best, abs(max_ending), abs(min_ending))
        return best
