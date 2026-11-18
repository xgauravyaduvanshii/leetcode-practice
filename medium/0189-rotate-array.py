# LeetCode 189. Rotate Array — Medium
# https://leetcode.com/problems/rotate-array/
# Submission 2198441103 — Accepted, Python3
#
# My thinking: reversing the whole array puts the
# last k numbers first, just in the wrong order.
# Reversing those k numbers fixes them, and
# reversing the rest fixes the other side — three
# reversals and the array is rotated in place.

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
