// LeetCode 1889. Minimum Space Wasted From Packaging — Hard
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/
// Submission 2201220489 — Accepted, Java
//
// My thinking: I pick one supplier, and every
// package takes the smallest box of theirs that
// fits it — so I sort the packages, walk each
// supplier's box sizes in order, and add up the
// waste band by band.

import java.util.*;

class Solution {
    public int minWastedSpace(int[] packages, int[][] boxes) {
        Arrays.sort(packages);
        int n = packages.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + packages[i];
        long ans = Long.MAX_VALUE;
        for (int[] supplier : boxes) {
            Arrays.sort(supplier);
            if (supplier[supplier.length - 1] < packages[n - 1]) continue;
            long waste = 0;
            int prev = 0;
            for (int b : supplier) {
                int idx = upperBound(packages, b, prev);
                waste += (long) (idx - prev) * b - (pref[idx] - pref[prev]);
                prev = idx;
                if (prev == n) break;
            }
            if (prev == n) ans = Math.min(ans, waste);
        }
        return ans == Long.MAX_VALUE ? -1 : (int) (ans % 1000000007);
    }

    private int upperBound(int[] a, int v, int lo) {
        int hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= v) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
