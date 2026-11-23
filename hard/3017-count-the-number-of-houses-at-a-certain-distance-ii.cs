// LeetCode 3017. Count the Number of Houses at a Certain Distance II — Hard
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/
// Submission 2201886226 — Accepted, C#
//
// My thinking: the extra street turns
// the houses from x to y into a cycle,
// with a plain line hanging off each
// end. I count the pairs inside each
// part on its own — lines by length,
// the cycle by going either way round
// — and the pairs across parts by how
// far each house sits from the end it
// hangs off, adding whole ranges at a
// time with a difference array.

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> CountOfPairs(int n, int x, int y) {
        if (x == y) {
            // No shortcut at all: a plain line of n houses.
            var line = new List<int>(n);
            for (int d = 1; d <= n; d++) {
                line.Add(d < n ? 2 * (n - d) : 0);
            }
            return line;
        }
        if (x > y) {
            int tmp = x;
            x = y;
            y = tmp;
        }
        int d = y - x;
        int leftLen = x - 1;
        int rightLen = n - y;
        int m = d + 1; // houses on the cycle, x..y
        long[] ans = new long[n + 1]; // ans[t] = unordered pairs at distance t

        // Pairs inside the left line and inside the right line.
        for (int t = 1; t < leftLen; t++) ans[t] += leftLen - t;
        for (int t = 1; t < rightLen; t++) ans[t] += rightLen - t;

        // Pairs inside the cycle: each house has two at every distance
        // below half the cycle, one at exactly half when the cycle is even.
        for (int t = 1; t <= (m - 1) / 2; t++) ans[t] += m;
        if (m % 2 == 0) ans[m / 2] += m / 2;

        // How many cycle houses sit at each cycle-distance from an end.
        int[] cntC = new int[m / 2 + 2];
        for (int j = 0; j < m; j++) {
            cntC[Math.Min(j, m - j)]++;
        }

        // Difference array for the cross-part range additions.
        long[] diff = new long[n + 3];
        Action<int, int, long> rangeAdd = (lo, hi, val) => {
            if (val == 0 || lo > hi) return;
            lo = Math.Max(lo, 1);
            hi = Math.Min(hi, n);
            if (lo > hi) return;
            diff[lo] += val;
            diff[hi + 1] -= val;
        };

        // Left line to cycle, and right line to cycle: a house i steps
        // from the end plus a cycle house v steps round the cycle.
        for (int v = 0; v < cntC.Length; v++) {
            if (cntC[v] != 0) {
                rangeAdd(v + 1, v + leftLen, cntC[v]);
                rangeAdd(v + 1, v + rightLen, cntC[v]);
            }
        }
        // Left line to right line: i steps out one side, j out the other,
        // one street across the shortcut.
        for (int i = 1; i <= leftLen; i++) {
            rangeAdd(i + 2, i + rightLen + 1, 1);
        }

        long run = 0;
        var res = new List<int>(n);
        for (int t = 1; t <= n; t++) {
            run += diff[t];
            ans[t] += run;
            // Every unordered pair is two ordered pairs.
            res.Add((int)(2 * ans[t]));
        }
        return res;
    }
}
