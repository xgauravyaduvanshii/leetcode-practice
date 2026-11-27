# 3354. Make Array Elements Equal to Zero (Easy)
# https://leetcode.com/problems/make-array-elements-equal-to-zero/
# Submission 2200007491 — Accepted, Python3
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # My thinking: I can only start from a zero.
        # From there I walk left or right, lowering each
        # number I step on by one, turning around when
        # it hits zero. A start counts if either
        # direction, or both, clears the whole array.
        def works(start: int, direction: int) -> bool:
            arr = nums[:]
            i = start
            d = direction
            while 0 <= i < len(arr):
                if arr[i] == 0:
                    i += d
                else:
                    arr[i] -= 1
                    d = -d
                    i += d
            return all(v == 0 for v in arr)

        count = 0
        for i, v in enumerate(nums):
            if v == 0:
                if works(i, 1):
                    count += 1
                if works(i, -1):
                    count += 1
        return count
