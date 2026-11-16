# LeetCode 628. Maximum Product of Three Numbers — Easy
# https://leetcode.com/problems/maximum-product-of-three-numbers/
# Submission 2197507539 — Accepted, Python3
#
# My thinking: after sorting, the biggest product
# comes from one of two groups — the three biggest
# numbers, or the two smallest (they might both be
# negative, and two negatives make a positive)
# times the biggest one. I take whichever is bigger.

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
