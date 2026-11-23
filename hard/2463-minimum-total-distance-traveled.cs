// LeetCode 2463. Minimum Total Distance Traveled — Hard
// https://leetcode.com/problems/minimum-total-distance-traveled/
// Submission 2201763446 — Accepted, C#
//
// My thinking: robots and factories both
// line up in order, so a factory only ever
// takes the next few robots in line — I
// sort both, then fill a table where each
// factory either sits out or takes a run
// of the robots still waiting.

using System;

public class Solution {
    public long MinimumTotalDistance(int[] robot, int[][] factory) {
        Array.Sort(robot);
        Array.Sort(factory, (a, b) => a[0].CompareTo(b[0]));
        int n = robot.Length, m = factory.Length;
        const long INF = long.MaxValue / 4;
        long[,] dp = new long[n + 1, m + 1];
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= m; j++)
                dp[i, j] = INF;
        for (int j = 0; j <= m; j++) dp[0, j] = 0;
        for (int j = 1; j <= m; j++) {
            int pos = factory[j - 1][0], limit = factory[j - 1][1];
            for (int i = 1; i <= n; i++) {
                long best = dp[i, j - 1];
                long run = 0;
                for (int t = 1; t <= Math.Min(limit, i); t++) {
                    run += Math.Abs((long)robot[i - t] - pos);
                    if (dp[i - t, j - 1] != INF)
                        best = Math.Min(best, dp[i - t, j - 1] + run);
                }
                dp[i, j] = best;
            }
        }
        return dp[n, m];
    }
}
