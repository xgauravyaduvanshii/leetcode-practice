# LeetCode 665. Non-decreasing Array — Medium
# https://leetcode.com/problems/non-decreasing-array/
# Submission 2198902631 — Accepted, Python3
#
# My thinking: the first dip can be fixed by
# lowering the left number or raising the right
# one, whichever keeps the neighbours in order. A
# second dip means one change is not enough.

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        fixed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if fixed:
                    return False
                fixed = True
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
        return True
