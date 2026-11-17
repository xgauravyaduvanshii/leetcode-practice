# LeetCode 2652. Sum Multiples — Easy
# https://leetcode.com/problems/sum-multiples/
# Submission 2197812182 — Accepted, Python3
#
# My thinking: I add up every number from 1 to n
# that is divisible by 3, 5, or 7.

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(x for x in range(1, n + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0)
