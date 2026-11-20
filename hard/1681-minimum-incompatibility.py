class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        # My thinking: with at most 16 numbers, list every
        # legal group once — no repeats inside, all the same
        # size — then build the answer group by group over
        # the bitmasks.
        n = len(nums)
        size = n // k
        INF = float("inf")
        cost = {}
        for mask in range(1 << n):
            if bin(mask).count("1") != size:
                continue
            vals = [nums[i] for i in range(n) if mask >> i & 1]
            if len(set(vals)) != size:
                continue
            cost[mask] = max(vals) - min(vals)
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            # pick the lowest unset bit to avoid duplicate work
            first = next((i for i in range(n) if not (mask >> i & 1)), None)
            if first is None:
                continue
            for sub, c in cost.items():
                if sub & mask:
                    continue
                if not (sub >> first & 1):
                    continue
                dp[mask | sub] = min(dp[mask | sub], dp[mask] + c)
        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != INF else -1
