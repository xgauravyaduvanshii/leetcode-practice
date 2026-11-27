// LeetCode 2499. Minimum Total Cost to Make Arrays Unequal — Hard
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/
// Submission 2201782888 — Accepted, C#
//
// My thinking: only the spots where the
// two arrays already match are broken —
// I pair those spots up, cheapest first.
// If one value fills more than half the
// broken spots, those spots cannot all be
// fixed among themselves, so I borrow
// good spots (two times the excess many),
// cheapest first, each one fitting neither
// side. With no dominant value the broken
// spots pair up on their own; when their
// count is odd the leftover borrows the
// cheapest fitting spot, good or already
// paired.

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public long MinimumTotalCost(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        var bad = new List<int>();
        var good = new List<int>();
        for (int i = 0; i < n; i++) {
            if (nums1[i] == nums2[i]) bad.Add(i);
            else good.Add(i);
        }
        if (bad.Count == 0) return 0;
        int m = bad.Count;
        var cnt = new Dictionary<int, int>();
        foreach (int i in bad) {
            cnt[nums1[i]] = cnt.GetValueOrDefault(nums1[i], 0) + 1;
        }
        int val = 0, mx = 0;
        foreach (var kv in cnt) {
            if (kv.Value > mx) { mx = kv.Value; val = kv.Key; }
        }
        long total = bad.Sum(i => (long)i);

        List<int> SuitableGood(int excludeVal) {
            var res = new List<int>();
            foreach (int j in good) {
                if (nums1[j] != excludeVal && nums2[j] != excludeVal) res.Add(j);
            }
            return res;
        }

        if (mx > m / 2) {
            int need = 2 * mx - m;
            var cand = SuitableGood(val);
            if (cand.Count < need) return -1;
            long extra = 0;
            for (int t = 0; t < need; t++) extra += cand[t];
            return total + extra;
        }
        if (m % 2 == 0) return total;
        int extraIdx = bad.Min();
        foreach (int j in good) {
            bool usable = false;
            foreach (int i in bad) {
                if (nums1[j] != nums2[i] && nums2[i] != nums2[j]) { usable = true; break; }
            }
            if (usable) { extraIdx = Math.Min(extraIdx, j); break; }
        }
        return total + extraIdx;
    }
}
