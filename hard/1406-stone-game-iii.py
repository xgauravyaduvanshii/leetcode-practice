class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        # My thinking: from each pile, taking one, two or
        # three stones earns their values minus whatever the
        # other player then earns — so work backwards keeping
        # the best difference.
        n = len(stoneValue)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + stoneValue[i]
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            best = float("-inf")
            for k in range(1, 4):
                if i + k <= n:
                    take = suffix[i] - suffix[i + k]
                    best = max(best, take - dp[i + k])
            dp[i] = best
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"
