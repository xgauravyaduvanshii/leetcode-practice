# LeetCode 27. Remove Element — Easy
# https://leetcode.com/problems/remove-element/
# Submission 2197280058 — Accepted, Python3
#
# My thinking: same two-pointer idea as the last one.
# I go through every number, and only keep the ones
# that are not the value to remove — I write them
# at the front, in order, and return how many I kept.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write = 0
        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        return write
