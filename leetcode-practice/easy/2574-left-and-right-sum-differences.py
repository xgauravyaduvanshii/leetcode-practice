# LeetCode 2574. Left and Right Sum Differences — Easy
# https://leetcode.com/problems/left-and-right-sum-differences/
# Submission 2197805407 — Accepted, Python3
#
# My thinking: I walk through the array keeping the
# sum of everything to the left. The right sum is
# the total minus the left sum minus the current
# element, and the answer at each spot is the
# absolute difference of the two.

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        res = []
        for x in nums:
            right = total - left - x
            res.append(abs(left - right))
            left += x
        return res
