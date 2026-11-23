// LeetCode 2188. Minimum Time to Finish the Race — Hard
// https://leetcode.com/problems/minimum-time-to-finish-the-race/
// Submission 2201605707 — Accepted, Java
//
// My thinking: a set of tyres only gets
// slower, so no stint is ever worth more
// than a handful of laps — I price the best
// stint of each length once, then chain
// stints together, paying the change each
// time except the first.

import java.util.Arrays;

class Solution {
    public int minimumFinishTime(int[][] tires, int changeTime, int numLaps) {
        int minF = Integer.MAX_VALUE;
        for (int[] t : tires) minF = Math.min(minF, t[0]);
        // Best time for a stint of x laps on one set of tyres.
        long[] best = new long[19];
        Arrays.fill(best, Long.MAX_VALUE);
        for (int[] t : tires) {
            int f = t[0], r = t[1];
            long time = 0;
            long cur = f;
            for (int x = 1; x <= 18; x++) {
                time += cur;
                best[x] = Math.min(best[x], time);
                if (cur > (long) changeTime + minF) break;
                cur *= r;
            }
        }
        long INF = Long.MAX_VALUE / 4;
        long[] dp = new long[numLaps + 1];
        Arrays.fill(dp, INF);
        dp[0] = -changeTime;
        for (int i = 1; i <= numLaps; i++) {
            for (int x = 1; x <= Math.min(i, 18); x++) {
                if (best[x] != Long.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i - x] + best[x] + changeTime);
                }
            }
        }
        return (int) dp[numLaps];
    }
}
