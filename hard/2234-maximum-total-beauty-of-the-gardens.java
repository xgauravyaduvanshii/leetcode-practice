// LeetCode 2234. Maximum Total Beauty of the Gardens — Hard
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/
// Submission 2201630672 — Accepted, Java
//
// My thinking: I sort the gardens, finish
// the biggest ones first, and spend what's
// left raising the smallest of the rest —
// for each count of finished gardens I
// binary-search the highest floor the rest
// can reach.

import java.util.Arrays;

class Solution {
    public long maximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        Arrays.sort(flowers);
        int n = flowers.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + flowers[i];
        long[] need = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            need[i] = need[i - 1] + Math.max(0, target - flowers[n - i]);
        }
        long ans = 0;
        for (int i = 0; i <= n; i++) {
            if (need[i] > newFlowers) break;
            long rem = newFlowers - need[i];
            if (i == n) {
                ans = Math.max(ans, (long) n * full);
                continue;
            }
            int m = n - i;
            int incomplete = lowerBound(flowers, target, 0, m);
            if (incomplete == 0) {
                ans = Math.max(ans, (long) n * full);
                continue;
            }
            int lo = 0, hi = target - 1, best = 0;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                int cnt = lowerBound(flowers, mid, 0, m);
                long cost = (long) cnt * mid - pref[cnt];
                if (cost <= rem) {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            ans = Math.max(ans, (long) i * full + (long) best * partial);
        }
        return ans;
    }

    private int lowerBound(int[] a, int value, int from, int to) {
        int lo = from, hi = to;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < value) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
