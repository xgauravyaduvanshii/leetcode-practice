# LeetCode 516. Longest Palindromic Subsequence — Medium
# https://leetcode.com/problems/longest-palindromic-subsequence/
# Submission 2198837269 — Accepted, Python3
#
# My thinking: for any stretch of the string, equal
# ends can both join the palindrome, and unequal
# ends force me to drop one of them. I build the
# answers up from short stretches to long ones.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
