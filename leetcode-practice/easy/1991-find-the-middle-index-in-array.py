# LeetCode 1991. Find the Middle Index in Array — Easy
# https://leetcode.com/problems/find-the-middle-index-in-array/
# Submission 2197607890 — Accepted, Python3
#
# My thinking: I keep the sum of everything to the
# left of the current index. The right side is the
# total minus the left sum minus the current value.
# When the two sides are equal, that index is the
# middle one.

class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == total - left - x:
                return i
            left += x
        return -1
