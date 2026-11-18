# LeetCode 962. Maximum Width Ramp — Medium
# https://leetcode.com/problems/maximum-width-ramp/
# Submission 2198977061 — Accepted, Python3
#
# My thinking: I collect the positions of
# decreasing values from the left — those are
# the only useful starts. Then I scan from the
# right, and every time a start fits under the
# current value, I take the widest ramp from it.

from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)
        best = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                best = max(best, j - stack.pop())
        return best
