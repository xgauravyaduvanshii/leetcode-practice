# LeetCode 2894. Divisible and Non-divisible Sums Difference — Easy
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
# Submission 2198693537 — Accepted, Python3
#
# My thinking: the total of 1 to n is easy, and the
# divisible part is m times the total of 1 to how many
# multiples fit. The answer is the total minus twice
# the divisible part — once to remove it, once more
# because the non-divisible sum subtracts it.

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        k = n // m
        divisible = m * k * (k + 1) // 2
        return total - 2 * divisible
