# LeetCode 324. Wiggle Sort II — Medium
# https://leetcode.com/problems/wiggle-sort-ii/
# Submission 2198746702 — Accepted, Python3
#
# My thinking: after sorting, the smaller half and
# the larger half never share a value at the
# boundary if I reverse both. Interleaving them —
# small, large, small, large — puts a small number
# before every large one and a large one before
# every small one, which is exactly the wiggle.

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        half = (len(nums) + 1) // 2
        small = nums[:half][::-1]
        large = nums[half:][::-1]
        nums[::2] = small
        nums[1::2] = large
