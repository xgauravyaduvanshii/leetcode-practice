# LeetCode 26. Remove Duplicates from Sorted Array — Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Submission 2197279754 — Accepted, Python3
#
# My thinking: the array is sorted, so duplicates sit
# next to each other. I keep a write pointer for where
# the next unique number should go, and scan with a
# read pointer — whenever I see a number different
# from the one just before it, it is new, so I write it.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write
