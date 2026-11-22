# LeetCode 1771. Maximize Palindrome Length From Subsequences — Hard
# https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/
# Submission 2201157136 — Accepted, Python3
#
# My thinking: the finished palindrome starts with
# a letter from the first word and ends with the
# same letter from the second word, so I try every
# such matching pair and fill the middle with the
# longest palindromic subsequence between them.

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        m = len(word1)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        ans = 0
        for i in range(m):
            for j in range(m, n):
                if s[i] == s[j]:
                    inner = dp[i + 1][j - 1] if j - i > 1 else 0
                    ans = max(ans, 2 + inner)
        return ans
