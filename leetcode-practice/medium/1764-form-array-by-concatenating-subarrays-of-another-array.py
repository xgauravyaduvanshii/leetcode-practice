# LeetCode 1764. Form Array by Concatenating Subarrays of Another Array — Medium
# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
# Submission 2199929145 — Accepted, Python3
#
# My thinking: I look for each group in turn,
# scanning forward from where the last one
# ended. If a group never appears after that
# point, the array cannot be formed.

from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        pos = 0
        for group in groups:
            found = False
            while pos + len(group) <= len(nums):
                if nums[pos:pos + len(group)] == group:
                    pos += len(group)
                    found = True
                    break
                pos += 1
            if not found:
                return False
        return True
