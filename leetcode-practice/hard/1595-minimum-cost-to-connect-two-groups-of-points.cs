using System;

public class Solution {
    public int ConnectTwoGroups(IList<IList<int>> cost) {
        // My thinking: every point on the left needs at least
        // one wire and every point on the right needs to be
        // reached — so remember which right points are already
        // covered, and let each left point add extra wires
        // where they come cheap.
        int size1 = cost.Count, size2 = cost[0].Count;
        const int INF = int.MaxValue / 2;
        int[] dp = new int[1 << size2];
        for (int m = 0; m < dp.Length; m++) dp[m] = INF;
        dp[0] = 0;
        for (int i = 0; i < size1; i++) {
            int[] ndp = new int[1 << size2];
            for (int m = 0; m < ndp.Length; m++) ndp[m] = INF;
            for (int mask = 0; mask < (1 << size2); mask++) {
                if (dp[mask] == INF) continue;
                for (int j = 0; j < size2; j++) {
                    int nmask = mask | (1 << j);
                    ndp[nmask] = Math.Min(ndp[nmask], dp[mask] + cost[i][j]);
                }
            }
            // point i may connect to more points in group 2
            for (int mask = 0; mask < (1 << size2); mask++) {
                if (ndp[mask] == INF) continue;
                for (int j = 0; j < size2; j++) {
                    if ((mask & (1 << j)) == 0) {
                        int nmask = mask | (1 << j);
                        ndp[nmask] = Math.Min(ndp[nmask], ndp[mask] + cost[i][j]);
                    }
                }
            }
            dp = ndp;
        }
        return dp[(1 << size2) - 1];
    }
}
