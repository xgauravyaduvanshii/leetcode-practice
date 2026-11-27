# LeetCode 456. 132 Pattern — Medium
# https://leetcode.com/problems/132-pattern/
# Submission 2198806386 — Accepted, Python3
#
# My thinking: scanning from the right, I keep a
# stack of candidates for the "3" and remember the
# biggest "2" I have popped so far. A number smaller
# than that remembered "2" completes the pattern.

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float("-inf")
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False
