class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        # My thinking: every point on the left needs at least
        # one wire and every point on the right needs to be
        # reached — so remember which right points are already
        # covered, and let each left point add extra wires
        # where they come cheap.
        size1, size2 = len(cost), len(cost[0])
        INF = float("inf")
        dp = [INF] * (1 << size2)
        dp[0] = 0
        for i in range(size1):
            ndp = [INF] * (1 << size2)
            for mask in range(1 << size2):
                if dp[mask] == INF:
                    continue
                for j in range(size2):
                    nmask = mask | (1 << j)
                    ndp[nmask] = min(ndp[nmask], dp[mask] + cost[i][j])
            # point i may connect to more points in group 2
            for mask in range(1 << size2):
                if ndp[mask] == INF:
                    continue
                for j in range(size2):
                    if not (mask >> j) & 1:
                        nmask = mask | (1 << j)
                        ndp[nmask] = min(ndp[nmask], ndp[mask] + cost[i][j])
            dp = ndp
        return dp[(1 << size2) - 1]
