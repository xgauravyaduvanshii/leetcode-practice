# LeetCode 1638. Count Substrings That Differ by One Character — Medium
# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
# Submission 2199899581 — Accepted, Python3
#
# My thinking: for every pair of starting
# positions I extend both substrings together,
# counting them while they differ in exactly
# one spot and stopping at the second
# difference.

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        total = 0
        for i in range(len(s)):
            for j in range(len(t)):
                diff = 0
                k = 0
                while i + k < len(s) and j + k < len(t):
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        total += 1
                    elif diff > 1:
                        break
                    k += 1
        return total
