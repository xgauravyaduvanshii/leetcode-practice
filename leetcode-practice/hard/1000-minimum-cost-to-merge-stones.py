class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        # My thinking: merging k piles costs their sum, so split
        # each interval into a first part and the rest, building the
        # cheapest way to shrink it down to one pile.
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1
        prefix = [0]
        for stone in stones:
            prefix.append(prefix[-1] + stone)
        INF = float("inf")
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = INF
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]
        return dp[0][n - 1]
