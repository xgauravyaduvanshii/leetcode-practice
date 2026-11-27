# LeetCode 421. Maximum XOR of Two Numbers in an Array — Medium
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# Submission 2198786176 — Accepted, Python3
#
# My thinking: I build the answer bit by bit from
# the top down, trying to set each bit to 1. A bit
# can be 1 exactly when two number-prefixes differ
# by that bit — I check that with a set of the
# prefixes seen so far.

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        best = 0
        mask = 0
        for bit in range(31, -1, -1):
            mask |= 1 << bit
            prefixes = {num & mask for num in nums}
            candidate = best | (1 << bit)
            if any((candidate ^ prefix) in prefixes for prefix in prefixes):
                best = candidate
        return best
