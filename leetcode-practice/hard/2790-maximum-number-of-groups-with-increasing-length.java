// LeetCode 2790. Maximum Number of Groups With Increasing Length — Hard
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/
// Submission 2201621423 — Accepted, Java
//
// My thinking: k groups must have strictly
// increasing sizes, so the smallest they can
// be is 1, 2, ..., k — and a number used at
// most L times can give at most one slot to
// each group, so for every t the t biggest
// groups need sum min(limit, t) to cover
// their sizes. That check is monotone in k,
// so I binary-search the biggest k that
// passes it for every t.

import java.util.Arrays;

class Solution {
    public int maximumGroups(int[] usageLimits) {
        Arrays.sort(usageLimits);
        int n = usageLimits.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + usageLimits[i];
        }
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (feasible(usageLimits, pref, n, mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }

    private boolean feasible(int[] limits, long[] pref, int n, int k) {
        // j counts the limits <= t; it only moves forward
        // as t grows, so this whole check is O(n + k).
        int j = 0;
        for (int t = 1; t <= k; t++) {
            while (j < n && limits[j] <= t) {
                j++;
            }
            long have = pref[j] + (long) t * (n - j);
            long need = (long) t * (2 * k - t + 1) / 2;
            if (have < need) {
                return false;
            }
        }
        return true;
    }
}
