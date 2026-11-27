# LeetCode 80. Remove Duplicates from Sorted Array II — Medium
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Submission 2203850118 — Accepted, Python3
#
# My thinking: I keep a write pointer that starts at 2, because the
# first two elements are always fine. For each later element I compare
# it with the element two places before the write pointer: if it is
# different, it is at most the second copy of its value, so I write it
# in; if it is the same, it would be a third copy and I skip it. The
# write pointer ends up as the new length.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        write = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        return write
