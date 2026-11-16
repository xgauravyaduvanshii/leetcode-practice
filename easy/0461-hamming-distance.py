# LeetCode 461. Hamming Distance — Easy
# https://leetcode.com/problems/hamming-distance/
# Submission 2197479622 — Accepted, Python3
#
# My thinking: XOR the two numbers — every bit where
# they differ becomes a 1. Then I just count how
# many 1s there are.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
