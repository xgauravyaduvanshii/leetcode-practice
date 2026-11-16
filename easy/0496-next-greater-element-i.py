# LeetCode 496. Next Greater Element I — Easy
# https://leetcode.com/problems/next-greater-element-i/
# Submission 2197485071 — Accepted, Python3
#
# My thinking: I scan nums2 with a stack that stays
# decreasing. When a bigger number arrives, it is
# the next greater element for everything smaller
# than it on the stack — I pop them and record it.
# Whatever is left on the stack has no greater
# element, so it gets -1.

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        for num in stack:
            next_greater[num] = -1
        return [next_greater[num] for num in nums1]
