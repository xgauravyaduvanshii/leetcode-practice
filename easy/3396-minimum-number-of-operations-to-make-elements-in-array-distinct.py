# 3396. Minimum Number of Operations to Make Elements in Array Distinct (Easy)
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
# Submission 2200013181 — Accepted, Python3
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # My thinking: each operation drops the first
        # three numbers. I count how many drops it
        # takes until no value appears twice — and the
        # numbers already distinct need no operation at
        # all.
        ops = 0
        while len(nums) != len(set(nums)):
            nums = nums[3:]
            ops += 1
        return ops
