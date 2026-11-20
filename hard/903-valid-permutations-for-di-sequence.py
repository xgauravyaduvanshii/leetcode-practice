class Solution:
    def numPermsDISequence(self, s: str) -> int:
        # My thinking: build the permutation left to right, tracking
        # only the relative rank of the last number — each D or I
        # step sums the ranks that can come before it.
        MOD = 10 ** 9 + 7
        dp = [1]
        for ch in s:
            m = len(dp)
            new = [0] * (m + 1)
            if ch == "I":
                running = 0
                for j in range(m + 1):
                    new[j] = running
                    if j < m:
                        running = (running + dp[j]) % MOD
            else:
                running = 0
                for j in range(m, -1, -1):
                    new[j] = running
                    if j > 0:
                        running = (running + dp[j - 1]) % MOD
            dp = new
        return sum(dp) % MOD
