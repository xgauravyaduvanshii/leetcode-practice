# LeetCode 2932. Maximum Strong Pair XOR I — Easy
# https://leetcode.com/problems/maximum-strong-pair-xor-i/
# Submission 2198701916 — Accepted, Python3
#
# My thinking: a pair is strong when the two numbers
# are close — their difference no bigger than the
# smaller one. The input is small, so I check every
# pair and keep the biggest xor among the strong ones.

from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        best = 0
        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    best = max(best, x ^ y)
        return best
