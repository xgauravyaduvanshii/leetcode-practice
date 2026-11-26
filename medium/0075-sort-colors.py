# LeetCode 75. Sort Colors — Medium
# https://leetcode.com/problems/sort-colors/
# Submission 2203844078 — Accepted, Python3
#
# My thinking: I keep three regions with three pointers — reds at the
# front, whites in the middle, blues at the back — and scan the middle
# region once. A 0 swaps to the front and both front pointers move, a
# 2 swaps to the back and the back pointer moves in, and a 1 is already
# in place, so I just move on. One pass, no extra space.

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1
