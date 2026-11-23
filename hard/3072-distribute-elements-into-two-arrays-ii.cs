// LeetCode 3072. Distribute Elements Into Two Arrays II — Hard
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/
// Submission 2201922738 — Accepted, C#
//
// My thinking: each step needs to know,
// for both arrays, how many of their
// numbers are bigger than the new one.
// I compress the values and keep a
// Fenwick tree per array, so each count
// is one prefix sum and each placement
// is one update. The tie-breaks follow
// the rules: bigger count wins, then
// the shorter array, then arr1.

using System;
using System.Collections.Generic;

public class Solution {
    private class Fenwick {
        private readonly int[] bit;
        public Fenwick(int n) { bit = new int[n + 1]; }
        public void Add(int i, int delta) {
            for (; i < bit.Length; i += i & -i) bit[i] += delta;
        }
        public int Sum(int i) {
            int s = 0;
            for (; i > 0; i -= i & -i) s += bit[i];
            return s;
        }
    }

    public int[] ResultArray(int[] nums) {
        var vals = new SortedSet<int>(nums);
        var sorted = new List<int>(vals);
        var rank = new Dictionary<int, int>();
        for (int i = 0; i < sorted.Count; i++) rank[sorted[i]] = i + 1;
        var bit1 = new Fenwick(sorted.Count);
        var bit2 = new Fenwick(sorted.Count);
        var arr1 = new List<int> { nums[0] };
        var arr2 = new List<int> { nums[1] };
        bit1.Add(rank[nums[0]], 1);
        bit2.Add(rank[nums[1]], 1);
        for (int t = 2; t < nums.Length; t++) {
            int x = nums[t];
            // Numbers <= x sit at ranks up to the upper bound.
            int r = sorted.BinarySearch(x);
            if (r < 0) r = ~r;
            else r = r + 1;
            int g1 = arr1.Count - bit1.Sum(r);
            int g2 = arr2.Count - bit2.Sum(r);
            if (g1 > g2 || (g1 == g2 && arr1.Count <= arr2.Count)) {
                arr1.Add(x);
                bit1.Add(rank[x], 1);
            } else {
                arr2.Add(x);
                bit2.Add(rank[x], 1);
            }
        }
        arr1.AddRange(arr2);
        return arr1.ToArray();
    }
}
