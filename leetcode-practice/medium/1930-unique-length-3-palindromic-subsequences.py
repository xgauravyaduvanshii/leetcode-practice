# LeetCode 1930. Unique Length-3 Palindromic Subsequences — Medium
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
# Submission 2201660994 — Accepted, Python3
#
# My thinking: a length-3 palindrome is
# one letter hugging any middle letter, so
# for each letter I look between its first
# and last sighting and count the distinct
# letters hiding there.

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        ans = 0
        for c in first:
            l, r = first[c], last[c]
            if l < r:
                ans += len(set(s[l + 1:r]))
        return ans
