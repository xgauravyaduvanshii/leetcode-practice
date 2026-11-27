# LeetCode 238. Product of Array Except Self — Medium
# https://leetcode.com/problems/product-of-array-except-self/
# Submission 2198724550 — Accepted, Python3
#
# My thinking: for each position the answer is the
# product of everything to its left times the product
# of everything to its right. I sweep once from the
# left collecting prefix products, then once from the
# right multiplying in the suffix products — no
# division, and only the answer array as extra space.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
