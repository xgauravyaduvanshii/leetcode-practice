# LeetCode 209. Minimum Size Subarray Sum — Medium
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Submission 2198450299 — Accepted, Python3
#
# My thinking: all the numbers are positive, so a
# window only grows to the right and shrinks from
# the left. I grow it until its sum reaches the
# target, then shrink it from the left as far as I
# can while the sum still reaches it, noting the
# shortest window I find. If no window ever
# reaches the target the answer is zero.

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float("inf")
        total = 0
        left = 0
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best == float("inf") else best
