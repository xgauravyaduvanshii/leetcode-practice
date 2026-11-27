# 3452. Sum of Good Numbers (Easy)
# https://leetcode.com/problems/sum-of-good-numbers/
# Submission 2200018903 — Accepted, Python3
from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        # My thinking: a number is good when it beats
        # the neighbour k spots away on both sides —
        # missing neighbours don't block it. I add up
        # all the good ones.
        total = 0
        for i, num in enumerate(nums):
            if i - k >= 0 and nums[i - k] >= num:
                continue
            if i + k < len(nums) and nums[i + k] >= num:
                continue
            total += num
        return total
