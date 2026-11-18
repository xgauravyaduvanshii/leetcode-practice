# LeetCode 260. Single Number III — Medium
# https://leetcode.com/problems/single-number-iii/
# Submission 2198726170 — Accepted, Python3
#
# My thinking: xoring everything cancels the pairs
# and leaves the xor of the two lonely numbers. Any
# bit set in that xor belongs to exactly one of them,
# so I split the array on that bit and xor each group
# — each group collapses to one of the two numbers.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
        lowest_bit = xor_all & -xor_all
        first = 0
        second = 0
        for num in nums:
            if num & lowest_bit:
                first ^= num
            else:
                second ^= num
        return [first, second]
