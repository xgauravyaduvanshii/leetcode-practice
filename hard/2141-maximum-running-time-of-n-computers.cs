// LeetCode 2141. Maximum Running Time of N Computers — Hard
// https://leetcode.com/problems/maximum-running-time-of-n-computers/
// Submission 2201586740 — Accepted, C#
//
// My thinking: in any window of T minutes a
// battery can give at most T minutes, so the
// whole room runs for T exactly when the
// capped-up total charge covers n times T —
// and that test only gets harder as T grows,
// so I binary-search the biggest T that passes.

public class Solution {
    public long MaxRunTime(int n, int[] batteries) {
        bool Feasible(long t) {
            long total = 0;
            foreach (int b in batteries) total += Math.Min((long)b, t);
            return total >= (long)n * t;
        }
        long lo = 0, hi = 0;
        foreach (int b in batteries) hi += b;
        hi = hi / n + 1;
        while (lo + 1 < hi) {
            long mid = lo + (hi - lo) / 2;
            if (Feasible(mid)) lo = mid;
            else hi = mid;
        }
        return lo;
    }
}
