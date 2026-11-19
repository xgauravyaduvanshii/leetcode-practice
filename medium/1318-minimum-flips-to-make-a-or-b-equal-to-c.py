# LeetCode 1318. Minimum Flips to Make a OR b Equal to c — Medium
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# Submission 2199031191 — Accepted, Python3
#
# My thinking: I check the numbers bit by bit.
# A zero bit in c needs every one bit in a or
# b flipped off; a one bit in c needs one flip
# only when both a and b have zero there.

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1
            if bit_c == 0:
                flips += bit_a + bit_b
            elif bit_a == 0 and bit_b == 0:
                flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
