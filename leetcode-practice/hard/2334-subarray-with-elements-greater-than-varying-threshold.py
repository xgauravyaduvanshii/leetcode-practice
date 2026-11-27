# LeetCode 2334. Subarray With Elements Greater Than Varying Threshold — Hard
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/
# Submission 2201685540 — Accepted, Python3
#
# My thinking: the smallest number in a
# stretch decides what that stretch can
# be — I give each number the widest
# stretch where it stays the smallest and
# keep the widest one that clears the bar.

class Solution:
    def validSubarraySize(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        left = [-1] * n
        stack = []
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] >= x:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while stack and nums[stack[-1]] > x:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        ans = -1
        for i, x in enumerate(nums):
            length = right[i] - left[i] - 1
            if length * x > threshold and length > ans:
                ans = length
        return ans
