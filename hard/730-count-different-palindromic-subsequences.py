class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        # My thinking: a distinct palindrome either skips the first
        # letter, skips the last, or uses both ends when they match —
        # and matching ends need the inner count plus the new one-
        # and two-letter palindromes they create.
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
                else:
                    low = i + 1
                    while low < j and s[low] != s[i]:
                        low += 1
                    high = j - 1
                    while high > i and s[high] != s[i]:
                        high -= 1
                    if low > high:
                        # No same letter inside: "aa" style.
                        dp[i][j] = (dp[i + 1][j - 1] * 2 + 2) % MOD
                    elif low == high:
                        # Exactly one same letter inside: "aaa" style.
                        dp[i][j] = (dp[i + 1][j - 1] * 2 + 1) % MOD
                    else:
                        dp[i][j] = (dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]) % MOD
        return dp[0][n - 1] % MOD
