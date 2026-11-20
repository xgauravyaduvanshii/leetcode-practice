class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        # My thinking: paint house by house, remembering the
        # last colour and how many neighbourhoods have formed
        # — a new neighbourhood starts whenever the colour
        # changes.
        INF = float("inf")
        dp = [[INF] * (target + 1) for _ in range(n + 1)]
        for color in range(1, n + 1):
            if houses[0] == 0:
                dp[color][1] = cost[0][color - 1]
            elif houses[0] == color:
                dp[color][1] = 0
        for i in range(1, m):
            new = [[INF] * (target + 1) for _ in range(n + 1)]
            for color in range(1, n + 1):
                if houses[i] != 0 and houses[i] != color:
                    continue
                paint = 0 if houses[i] == color else cost[i][color - 1]
                for groups in range(1, target + 1):
                    best = INF
                    for prev in range(1, n + 1):
                        if prev == color:
                            if dp[prev][groups] != INF:
                                best = min(best, dp[prev][groups])
                        elif groups > 1 and dp[prev][groups - 1] != INF:
                            best = min(best, dp[prev][groups - 1])
                    if best != INF:
                        new[color][groups] = best + paint
            dp = new
        answer = min(dp[color][target] for color in range(1, n + 1))
        return -1 if answer == INF else answer
