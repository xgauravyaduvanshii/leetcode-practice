# LeetCode 2148. Count Elements With Strictly Smaller and Greater Elements — Easy
# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/
# Submission 2197614934 — Accepted, Python3
#
# My thinking: an element counts when some element is
# smaller and some element is bigger than it. That
# is exactly the elements that are neither the
# minimum nor the maximum.

class Solution:
    def countElements(self, nums: list[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return sum(1 for x in nums if mn < x < mx)
