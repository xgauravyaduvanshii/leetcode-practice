# LeetCode 2472. Maximum Number of Non-overlapping Palindrome Substrings — Hard
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
# Submission 2201768309 — Accepted, Python3
#
# My thinking: a palindrome I take can
# only end where one starts — I first
# learn which stretches read the same
# backwards, then walk the string once,
# either skipping the next character or
# closing the best palindrome that ends
# here and counting it.

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            pal[i][i + 1] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length
                if s[i] == s[j - 1] and (length <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i):
                if i - j >= k and pal[j][i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n]
