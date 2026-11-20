class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        # My thinking: sort the houses, then a mailbox always
        # sits on the middle house of its stretch — so the
        # cost of each stretch is known, and the rest is
        # splitting the street into k stretches.
        houses.sort()
        n = len(houses)
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                cost[i][j] = sum(abs(houses[t] - houses[mid]) for t in range(i, j + 1))
        INF = float("inf")
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for boxes in range(1, k + 1):
            for end in range(1, n + 1):
                for start in range(end):
                    if dp[boxes - 1][start] != INF:
                        dp[boxes][end] = min(dp[boxes][end], dp[boxes - 1][start] + cost[start][end - 1])
        return dp[k][n]
