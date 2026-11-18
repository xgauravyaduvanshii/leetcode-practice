# LeetCode 357. Count Numbers with Unique Digits — Medium
# https://leetcode.com/problems/count-numbers-with-unique-digits/
# Submission 2198757113 — Accepted, Python3
#
# My thinking: for numbers of each length I count
# the choices digit by digit — 9 ways for the first
# digit, then 9, 8, 7 and so on for the rest — and
# add up the counts for every length up to n.

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        total = 10
        unique = 9
        available = 9
        for _ in range(2, min(n, 10) + 1):
            unique *= available
            available -= 1
            total += unique
        return total
