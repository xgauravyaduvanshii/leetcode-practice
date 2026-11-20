public class Solution {
    public int MinCost(int[] houses, int[][] cost, int m, int n, int target) {
        // My thinking: paint house by house, remembering the
        // last colour and how many neighbourhoods have formed
        // — a new neighbourhood starts whenever the colour
        // changes.
        const int INF = int.MaxValue / 2;
        int[,] dp = new int[n + 1, target + 1];
        for (int c = 0; c <= n; c++)
            for (int g = 0; g <= target; g++) dp[c, g] = INF;
        for (int color = 1; color <= n; color++) {
            if (houses[0] == 0) dp[color, 1] = cost[0][color - 1];
            else if (houses[0] == color) dp[color, 1] = 0;
        }
        for (int i = 1; i < m; i++) {
            int[,] next = new int[n + 1, target + 1];
            for (int c = 0; c <= n; c++)
                for (int g = 0; g <= target; g++) next[c, g] = INF;
            for (int color = 1; color <= n; color++) {
                if (houses[i] != 0 && houses[i] != color) continue;
                int paint = houses[i] == color ? 0 : cost[i][color - 1];
                for (int groups = 1; groups <= target; groups++) {
                    int best = INF;
                    for (int prev = 1; prev <= n; prev++) {
                        if (prev == color) {
                            if (dp[prev, groups] != INF) best = System.Math.Min(best, dp[prev, groups]);
                        } else if (groups > 1 && dp[prev, groups - 1] != INF) {
                            best = System.Math.Min(best, dp[prev, groups - 1]);
                        }
                    }
                    if (best != INF) next[color, groups] = best + paint;
                }
            }
            dp = next;
        }
        int answer = INF;
        for (int color = 1; color <= n; color++) answer = System.Math.Min(answer, dp[color, target]);
        return answer == INF ? -1 : answer;
    }
}
