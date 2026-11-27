# LeetCode 503. Next Greater Element II — Medium
# https://leetcode.com/problems/next-greater-element-ii/
# Submission 2198833238 — Accepted, Python3
#
# My thinking: the array wraps around, so I scan
# it twice from the right with a decreasing stack.
# The stack top is the next greater element for
# everything smaller than it, and the second pass
# fills in the answers the first pass could not see.

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n - 1, -1, -1):
            index = i % n
            while stack and nums[stack[-1]] <= nums[index]:
                stack.pop()
            if stack:
                result[index] = nums[stack[-1]]
            stack.append(index)
        return result
