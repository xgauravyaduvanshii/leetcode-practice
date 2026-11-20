class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # My thinking: adding the number n + 1 to a permutation of n
        # creates 0..n new inversions, so each row is a sliding
        # window sum of the row before.
        MOD = 10 ** 9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for size in range(1, n + 1):
            new = [0] * (k + 1)
            window = 0
            for j in range(k + 1):
                window = (window + dp[j]) % MOD
                if j - size >= 0:
                    window = (window - dp[j - size]) % MOD
                new[j] = window
            dp = new
        return dp[k] % MOD
