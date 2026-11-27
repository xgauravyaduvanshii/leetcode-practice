# LeetCode 342. Power of Four — Easy
# https://leetcode.com/problems/power-of-four/
# Submission 2197464060 — Accepted, Python3
#
# My thinking: a power of four is a power of two with
# its single set bit in an even position. The power
# of two check is n & (n - 1) == 0, and n % 3 == 1
# keeps only the bits in even positions (4^k leaves
# remainder 1 when divided by 3).

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
