# LeetCode 2869. Minimum Operations to Collect Elements — Easy
# https://leetcode.com/problems/minimum-operations-to-collect-elements/
# Submission 2198425639 — Accepted, Python3
#
# My thinking: each operation takes the last element
# off, so I walk the list backwards collecting the
# values from 1 to k that I still need. As soon as
# I have seen them all, the number of elements I
# walked past is the number of operations.

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if 1 <= nums[i] <= k:
                seen.add(nums[i])
            if len(seen) == k:
                return len(nums) - i
        return len(nums)
