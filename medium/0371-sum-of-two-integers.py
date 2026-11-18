# LeetCode 371. Sum of Two Integers — Medium
# https://leetcode.com/problems/sum-of-two-integers/
# Submission 2198758810 — Accepted, Python3
#
# My thinking: adding without + is just xor for the
# sum bits and AND-shifted for the carries. I repeat
# both steps until no carry is left, working inside
# a 32-bit mask and converting the result back to a
# signed number at the end.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
