# LeetCode 1835. Find XOR Sum of All Pairs Bitwise AND — Hard
# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/
# Submission 2201192312 — Accepted, Python3
#
# My thinking: a bit survives the xor of all
# pairs exactly when it is set in an odd number
# of entries on both sides — which is just the
# xor of each array, anded together.

class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        x1 = 0
        for v in arr1:
            x1 ^= v
        x2 = 0
        for v in arr2:
            x2 ^= v
        return x1 & x2
