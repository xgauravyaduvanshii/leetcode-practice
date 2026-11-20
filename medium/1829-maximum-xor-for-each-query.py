# LeetCode 1829. Maximum XOR for Each Query — Medium
# https://leetcode.com/problems/maximum-xor-for-each-query/
# Submission 2199944899 — Accepted, Python3
#
# My thinking: removing the last element
# undoes one xor, so the best query answer
# is always the running xor flipped inside
# the bit mask. I walk the array backwards,
# answering and un-xoring as I go.

from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        xor = 0
        for num in nums:
            xor ^= num
        result = []
        for num in reversed(nums):
            result.append(xor ^ mask)
            xor ^= num
        return result
