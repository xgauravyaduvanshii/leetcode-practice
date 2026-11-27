# LeetCode 1752. Check if Array Is Sorted and Rotated — Easy
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Submission 2197597033 — Accepted, Python3
#
# My thinking: a sorted-and-rotated array has at
# most one "drop" — a place where a number is
# bigger than the next one (wrapping around to the
# start). I count the drops; one or none means it
# is sorted and rotated.

class Solution:
    def check(self, nums: list[int]) -> bool:
        drops = sum(1 for i in range(len(nums)) if nums[i] > nums[(i + 1) % len(nums)])
        return drops <= 1
