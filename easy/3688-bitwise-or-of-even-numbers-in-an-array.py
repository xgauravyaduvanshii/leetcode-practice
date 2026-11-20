# 3688. Bitwise OR of Even Numbers in an Array (Easy)
# https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/
# Submission 2200043939 — Accepted, Python3
from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        # My thinking: OR together every even number
        # in the array. If there is no even number at
        # all, the answer is zero.
        result = 0
        for num in nums:
            if num % 2 == 0:
                result |= num
        return result
