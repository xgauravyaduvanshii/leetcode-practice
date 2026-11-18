# LeetCode 442. Find All Duplicates in an Array — Medium
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Submission 2198795991 — Accepted, Python3
#
# My thinking: each value points at its own index,
# so I flip the sign there as a marker. Flipping an
# already negative slot means the value showed up
# before — that is a duplicate.

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]
        return duplicates
