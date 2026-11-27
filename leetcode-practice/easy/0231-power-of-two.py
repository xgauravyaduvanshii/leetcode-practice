# LeetCode 231. Power of Two — Easy
# https://leetcode.com/problems/power-of-two/
# Submission 2197454873 — Accepted, Python3
#
# My thinking: a power of two has exactly one bit set.
# So n and (n - 1) share no bits at all — their AND
# is zero. I also have to rule out zero and negatives
# first.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
