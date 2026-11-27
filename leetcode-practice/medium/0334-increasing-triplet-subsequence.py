# LeetCode 334. Increasing Triplet Subsequence — Medium
# https://leetcode.com/problems/increasing-triplet-subsequence/
# Submission 2198748876 — Accepted, Python3
#
# My thinking: I only need the smallest number seen
# so far and the smallest number bigger than it. If
# a third number arrives bigger than both, the
# triplet exists — and keeping both values as small
# as possible gives every later number its best
# chance.

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
