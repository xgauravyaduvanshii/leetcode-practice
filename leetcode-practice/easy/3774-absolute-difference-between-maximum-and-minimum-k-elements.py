# 3774. Absolute Difference Between Maximum and Minimum K Elements (Easy)
# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/
# Submission 2200063326 — Accepted, Python3
from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        # My thinking: add up the k biggest numbers and
        # the k smallest numbers, and take how far
        # apart those two sums are.
        nums = sorted(nums)
        return abs(sum(nums[-k:]) - sum(nums[:k]))
