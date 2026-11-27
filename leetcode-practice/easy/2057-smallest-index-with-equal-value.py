# LeetCode 2057. Smallest Index With Equal Value — Easy
# https://leetcode.com/problems/smallest-index-with-equal-value/
# Submission 2197611184 — Accepted, Python3
#
# My thinking: I scan the array from the left and
# return the first index where i % 10 equals the
# value at that index. If none matches, the answer
# is -1.

class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i, x in enumerate(nums):
            if i % 10 == x:
                return i
        return -1
