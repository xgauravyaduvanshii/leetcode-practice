# LeetCode 912. Sort an Array — Medium
# https://leetcode.com/problems/sort-an-array/
# Submission 2198968659 — Accepted, Python3
#
# My thinking: the problem forbids the built-in
# sort, so I sort it myself with merge sort —
# split the list in half, sort each half, then
# merge the two sorted halves back together.

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
