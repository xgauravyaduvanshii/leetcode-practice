// LeetCode 3624. Number of Integers With Popcount-Depth Equal to K II — Hard
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/
// Submission 2202886989 — Accepted, C#
using System.Collections.Generic;

public class Solution {
    private int Depth(long x) {
        // My thinking: the popcount-depth of a number up to 10^15
        // is at most 4, so every value falls into one of six depth
        // classes. I keep one Fenwick tree per depth, so a range
        // query is a single range sum on the tree for k, and an
        // update just moves one index between two trees. A query
        // for k = 5 always answers 0, since no number here reaches
        // depth 5.
        int d = 0;
        while (x != 1) {
            int c = 0;
            while (x > 0) { c += (int)(x & 1); x >>= 1; }
            x = c;
            d++;
        }
        return d;
    }

    private class Fenwick {
        private int n;
        private int[] bit;
        public Fenwick(int n) { this.n = n; bit = new int[n + 1]; }
        public void Add(int i, int delta) {
            i++;
            while (i <= n) { bit[i] += delta; i += i & -i; }
        }
        private int Sum(int i) {
            i++;
            int s = 0;
            while (i > 0) { s += bit[i]; i -= i & -i; }
            return s;
        }
        public int RangeSum(int l, int r) {
            return Sum(r) - (l > 0 ? Sum(l - 1) : 0);
        }
    }

    public IList<int> PopcountDepth(int[] nums, int[][] queries) {
        int n = nums.Length;
        var bits = new Fenwick[6];
        for (int i = 0; i < 6; i++) bits[i] = new Fenwick(n);
        var depths = new int[n];
        for (int i = 0; i < n; i++) {
            depths[i] = Depth(nums[i]);
            bits[depths[i]].Add(i, 1);
        }
        var ans = new List<int>();
        foreach (var q in queries) {
            if (q[0] == 1) {
                int l = q[1], r = q[2], k = q[3];
                ans.Add(k >= 0 && k < 6 ? bits[k].RangeSum(l, r) : 0);
            } else {
                int idx = q[1], val = q[2];
                int oldD = depths[idx];
                int newD = Depth(val);
                if (oldD != newD) {
                    bits[oldD].Add(idx, -1);
                    bits[newD].Add(idx, 1);
                    depths[idx] = newD;
                }
                nums[idx] = val;
            }
        }
        return ans;
    }
}
