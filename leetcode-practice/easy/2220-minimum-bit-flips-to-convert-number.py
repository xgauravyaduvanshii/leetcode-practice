# LeetCode 2220. Minimum Bit Flips to Convert Number — Easy
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
# Submission 2197618398 — Accepted, Python3
#
# My thinking: xoring the two numbers marks exactly
# the bit positions where they differ. Counting the
# 1 bits in that xor gives the number of flips.

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')
