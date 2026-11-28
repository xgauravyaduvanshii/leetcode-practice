# LeetCode 2575. Find the Divisibility Array of a String — Medium
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/
# Submission 2205080486 — Accepted, Python3
#
# My thinking: the prefix value can be huge, but only its
# remainder modulo m matters. Carry the remainder forward one
# digit at a time; a prefix is divisible exactly when the
# remainder hits zero.
class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        ans = []
        rem = 0
        for ch in word:
            rem = (rem * 10 + (ord(ch) - 48)) % m
            ans.append(1 if rem == 0 else 0)
        return ans
