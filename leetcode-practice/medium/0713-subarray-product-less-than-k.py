# LeetCode 713. Subarray Product Less Than K — Medium
# https://leetcode.com/problems/subarray-product-less-than-k/
# Submission 2198917825 — Accepted, Python3
#
# My thinking: I grow a window from the right and
# shrink it from the left until its product is
# under k. Every window ending at the right edge
# is then valid, so I add its length to the count.

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        total = 0
        product = 1
        left = 0
        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product //= nums[left]
                left += 1
            total += right - left + 1
        return total
