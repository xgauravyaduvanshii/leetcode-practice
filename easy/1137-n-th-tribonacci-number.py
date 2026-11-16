# LeetCode 1137. N-th Tribonacci Number — Easy
# https://leetcode.com/problems/n-th-tribonacci-number/
# Submission 2197559304 — Accepted, Python3
#
# My thinking: each Tribonacci number is the sum of
# the three before it, starting 0, 1, 1. I keep
# the last three values and roll them forward n
# times — after n steps, the first of the three is
# the answer.

class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a
