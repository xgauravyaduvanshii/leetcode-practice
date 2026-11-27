# LeetCode 392. Is Subsequence — Easy
# https://leetcode.com/problems/is-subsequence/
# Submission 2197470574 — Accepted, Python3
#
# My thinking: I walk through t once, and every time
# I see the next letter I am waiting for in s, I
# move on to the next one. If I get through all of
# s that way, it is a subsequence.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)
