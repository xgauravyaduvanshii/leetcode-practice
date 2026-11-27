# LeetCode 1837. Sum of Digits in Base K — Easy
# https://leetcode.com/problems/sum-of-digits-in-base-k/
# Submission 2197600563 — Accepted, Python3
#
# My thinking: I convert n to base k digit by digit
# — each step takes n % k as a digit and divides n
# by k — and add up all the digits as I go.

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total = 0
        while n:
            total += n % k
            n //= k
        return total
