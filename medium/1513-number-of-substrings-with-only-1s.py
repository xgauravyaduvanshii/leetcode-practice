# LeetCode 1513. Number of Substrings With Only 1s — Medium
# https://leetcode.com/problems/number-of-substrings-with-only-1s/
# Submission 2199866805 — Accepted, Python3
#
# My thinking: each run of ones of length L
# holds L choices for where a substring ends.
# I add the run length as it grows and reset
# it on every zero.

class Solution:
    def numSub(self, s: str) -> int:
        total = 0
        run = 0
        for ch in s:
            if ch == "1":
                run += 1
                total += run
            else:
                run = 0
        return total % (10 ** 9 + 7)
