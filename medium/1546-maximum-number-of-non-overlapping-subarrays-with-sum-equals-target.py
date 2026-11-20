# LeetCode 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target — Medium
# https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
# Submission 2199874381 — Accepted, Python3
#
# My thinking: I scan prefix sums, and the
# moment one completes a subarray hitting the
# target I take it and start fresh. Taking the
# earliest possible subarray always leaves
# the most room for the rest.

from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}
        prefix = 0
        count = 0
        for value in nums:
            prefix += value
            if prefix - target in seen:
                count += 1
                seen = {0}
                prefix = 0
            else:
                seen.add(prefix)
        return count
