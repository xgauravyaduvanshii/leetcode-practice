# LeetCode 191. Number of 1 Bits — Easy
# https://leetcode.com/problems/number-of-1-bits/
# Submission 2197449327 — Accepted, Python3
#
# My thinking: I look at the last bit of the number —
# if it is 1, I count it — then I shift the number
# right by one and do the same again until nothing
# is left.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
