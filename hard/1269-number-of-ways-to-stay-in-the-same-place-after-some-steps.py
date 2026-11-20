class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # My thinking: after i steps you can only be within i
        # of the start, so the walk stays on a short strip —
        # count the ways step by step.
        MOD = 10 ** 9 + 7
        width = min(arrLen, steps + 1)
        dp = [0] * width
        dp[0] = 1
        for _ in range(steps):
            new_dp = [0] * width
            for i in range(width):
                if dp[i] == 0:
                    continue
                new_dp[i] = (new_dp[i] + dp[i]) % MOD
                if i > 0:
                    new_dp[i - 1] = (new_dp[i - 1] + dp[i]) % MOD
                if i + 1 < width:
                    new_dp[i + 1] = (new_dp[i + 1] + dp[i]) % MOD
            dp = new_dp
        return dp[0]
