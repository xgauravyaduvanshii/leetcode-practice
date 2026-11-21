class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        # My thinking: the tallest stick splits the row — put it at the
        # right end and the sticks to its left form a smaller visible
        # arrangement, or place it anywhere else and it hides behind a
        # taller stick. That gives the Stirling numbers of the first kind:
        # dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j], all modulo 1e9+7.
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]) % MOD
        return dp[n][k]
