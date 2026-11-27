# LeetCode 326. Power of Three — Easy
# https://leetcode.com/problems/power-of-three/
# Submission 2197463531 — Accepted, Python3
#
# My thinking: the biggest power of 3 that fits in a
# 32-bit signed integer is 3^19 = 1162261467. Every
# smaller power of 3 divides it evenly, and nothing
# else does (apart from 1, which is 3^0). So one
# divisibility check is enough.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
