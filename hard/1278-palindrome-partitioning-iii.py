class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # My thinking: first count, for every substring, how many
        # changes make it a palindrome — then split the string
        # into k parts as cheaply as possible.
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])
        INF = float("inf")
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for parts in range(1, min(i, k) + 1):
                for j in range(parts - 1, i):
                    dp[i][parts] = min(dp[i][parts], dp[j][parts - 1] + cost[j][i - 1])
        return dp[n][k]
