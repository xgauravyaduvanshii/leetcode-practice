# LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I — Easy
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
# Submission 2198715015 — Accepted, Python3
#
# My thinking: the first subarray must start with the
# first element, so its cost is fixed. The other two
# subarrays just need the two smallest remaining
# starting elements — the two smallest numbers after
# the first one.

from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        rest = sorted(nums[1:])
        return nums[0] + rest[0] + rest[1]
