class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # My thinking: build the array left to right, tracking
        # the biggest value seen and how many times it changed
        # — each new value either stays under the maximum or
        # raises it.
        MOD = 10 ** 9 + 7
        if k == 0:
            return 0
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        for v in range(1, m + 1):
            dp[v][1] = 1
        for _ in range(1, n):
            new = [[0] * (k + 1) for _ in range(m + 1)]
            for c in range(1, k + 1):
                prefix = 0
                for v in range(1, m + 1):
                    # append a value <= v: v choices, cost stays c
                    new[v][c] = (new[v][c] + dp[v][c] * v) % MOD
                    # append a value > v: the new max is v, cost c+1
                    # — every smaller max contributes once
                    if c < k:
                        new[v][c + 1] = (new[v][c + 1] + prefix) % MOD
                    prefix = (prefix + dp[v][c]) % MOD
            dp = new
        return sum(dp[v][k] for v in range(1, m + 1)) % MOD
