# LeetCode 115. Distinct Subsequences — Hard
# https://leetcode.com/problems/distinct-subsequences/
# Submission 2198384294 — Accepted, Python3
#
# My thinking: I count, for each prefix of t, how
# many ways it appears as a subsequence of s so
# far. The empty prefix always has one way. When I
# meet a new character of s, I update the counts
# from the back, adding the ways to form the prefix
# without this character whenever it matches. One
# row of counts is enough.

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for ch in s:
            for j in range(len(t) - 1, -1, -1):
                if ch == t[j]:
                    dp[j + 1] += dp[j]
        return dp[len(t)]
