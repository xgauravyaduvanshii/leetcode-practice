class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        # My thinking: count the ways to pick crimes within n members
        # and at least minProfit — cap the profit dimension at the
        # target so the table stays small.
        MOD = 10 ** 9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for members, gain in zip(group, profit):
            for used in range(n - members, -1, -1):
                for p in range(minProfit + 1):
                    new_p = min(minProfit, p + gain)
                    dp[used + members][new_p] = (dp[used + members][new_p] + dp[used][p]) % MOD
        return sum(dp[used][minProfit] for used in range(n + 1)) % MOD
