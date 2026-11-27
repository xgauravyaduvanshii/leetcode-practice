# LeetCode 1913. Maximum Product Difference Between Two Pairs — Easy
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
# Submission 2197604276 — Accepted, Python3
#
# My thinking: to make the difference as big as
# possible, I want the biggest product and the
# smallest product. After sorting, the two largest
# numbers give the biggest product and the two
# smallest give the smallest one.

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
