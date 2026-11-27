# LeetCode 1922. Count Good Numbers — Medium
# https://leetcode.com/problems/count-good-numbers/
# Submission 2201609968 — Accepted, Python3
#
# My thinking: a digit string may start with
# zero, so every even place has five even
# digits to choose from and every odd place
# has four primes — multiply the choices.

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        even = (n + 1) // 2
        odd = n // 2
        return pow(5, even, MOD) * pow(4, odd, MOD) % MOD
