# LeetCode 2413. Smallest Even Multiple — Easy
# https://leetcode.com/problems/smallest-even-multiple/
# Submission 2197780894 — Accepted, Python3
#
# My thinking: if n is already even it is its own
# smallest even multiple; if it is odd, doubling it
# gives the smallest even multiple.

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2
