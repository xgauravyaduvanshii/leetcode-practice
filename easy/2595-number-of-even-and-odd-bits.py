# LeetCode 2595. Number of Even and Odd Bits — Easy
# https://leetcode.com/problems/number-of-even-and-odd-bits/
# Submission 2197808223 — Accepted, Python3
#
# My thinking: I read the bits of n from the least
# significant up, counting the set bits at even
# positions and at odd positions separately.

class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        even = odd = 0
        i = 0
        while n:
            if n & 1:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            i += 1
        return [even, odd]
