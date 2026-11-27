# LeetCode 2320. Count Number of Ways to Place Houses — Medium
# https://leetcode.com/problems/count-number-of-ways-to-place-houses/
# Submission 2204685520 — Accepted, Python3
#
# My thinking: one side of the street is a Fibonacci count — with n plots
# the number of ways to place houses with no two adjacent is Fib(n+2).
# I build it iteratively (a, b = 1, 2 rolling forward), and the two sides
# are independent, so the answer is that count squared, all modulo 10^9+7.
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a, b = 1, 2
        for _ in range(n - 1):
            a, b = b, (a + b) % MOD
        return b * b % MOD
