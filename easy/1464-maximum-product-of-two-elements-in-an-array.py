# LeetCode 1464. Maximum Product of Two Elements in an Array — Easy
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Submission 2197581054 — Accepted, Python3
#
# My thinking: the best product comes from the two
# biggest numbers. I sort the array, take the last
# two, subtract 1 from each, and multiply them.

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
