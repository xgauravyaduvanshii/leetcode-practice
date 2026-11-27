# 3411. Maximum Subarray With Equal Products (Easy)
# https://leetcode.com/problems/maximum-subarray-with-equal-products/
# Submission 2200014135 — Accepted, Python3
import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # My thinking: a subarray's product equals its
        # LCM exactly when no prime is shared between
        # two numbers in it — so I grow each subarray
        # and stop as soon as two numbers share a
        # factor. The longest one I find is the answer.
        best = 1
        for start in range(len(nums)):
            prod = 1
            lcm = 1
            for end in range(start, len(nums)):
                prod *= nums[end]
                lcm = lcm * nums[end] // math.gcd(lcm, nums[end])
                if prod != lcm:
                    break
                best = max(best, end - start + 1)
        return best
