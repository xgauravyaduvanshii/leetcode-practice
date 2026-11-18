# LeetCode 2980. Check if Bitwise OR Has Trailing Zeros — Easy
# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/
# Submission 2198713344 — Accepted, Python3
#
# My thinking: the OR of two numbers is even exactly
# when both numbers are even. So the answer is yes
# whenever the array holds at least two even numbers.

from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        evens = sum(1 for num in nums if num % 2 == 0)
        return evens >= 2
