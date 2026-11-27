# LeetCode 565. Array Nesting — Medium
# https://leetcode.com/problems/array-nesting/
# Submission 2198872332 — Accepted, Python3
#
# My thinking: following the jumps from a number
# walks a chain that never branches, so I mark
# every number I visit and only start a fresh walk
# from numbers I have not seen. The longest walk
# wins.

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = [False] * len(nums)
        best = 0
        for start in range(len(nums)):
            if seen[start]:
                continue
            length = 0
            current = start
            while not seen[current]:
                seen[current] = True
                current = nums[current]
                length += 1
            best = max(best, length)
        return best
