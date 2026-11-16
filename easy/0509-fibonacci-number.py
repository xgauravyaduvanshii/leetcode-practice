# LeetCode 509. Fibonacci Number — Easy
# https://leetcode.com/problems/fibonacci-number/
# Submission 2197487672 — Accepted, Python3
#
# My thinking: I only need the last two numbers. I
# start with 0 and 1, and step forward n times —
# each step the new number is the sum of the two
# before it.

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
