# LeetCode 693. Binary Number with Alternating Bits — Easy
# https://leetcode.com/problems/binary-number-with-alternating-bits/
# Submission 2197515348 — Accepted, Python3
#
# My thinking: I look at the binary digits of the
# number two at a time. If any two neighbours are
# the same, the bits do not alternate. If I get
# through them all without finding a pair like
# that, they do.

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)[2:]
        for i in range(1, len(bits)):
            if bits[i] == bits[i - 1]:
                return False
        return True
