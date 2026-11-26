// LeetCode 3939. Count Non Adjacent Subsets in a Rooted Tree — Hard
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/
// Submission 2203433630 — Accepted, C#
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;

    public int CountValidSubsets(int[] parent, int[] nums, int k) {
        // My thinking: a tree DP with two states per node.
        // dp0[u] counts the ways in u's subtree with sums
        // by residue mod k when u is not selected, dp1[u]
        // the same when u is selected. A child contributes
        // dp0 + dp1 to a non-selected parent (the child
        // may be either) but only dp0 to a selected parent
        // (no two adjacent nodes may both be selected).
        // Merging a child is a knapsack convolution over
        // residues: new[(a + b) % k] += dp[a] * child[b].
        // Since parent[i] < i, processing nodes in reverse
        // index order finalises every child before its
        // parent. The answer is the residue-0 count at the
        // root over both states, minus 1 for the empty
        // subset.
        int n = parent.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) children[parent[i]].Add(i);
        var dp0 = new long[n][];
        var dp1 = new long[n][];
        for (int u = n - 1; u >= 0; u--) {
            var cur0 = new long[k];
            cur0[0] = 1;
            var cur1 = new long[k];
            cur1[((nums[u] % k) + k) % k] = 1;
            foreach (int ch in children[u]) {
                var tot = new long[k];
                for (int r = 0; r < k; r++) {
                    tot[r] = (dp0[ch][r] + dp1[ch][r]) % MOD;
                }
                var nxt0 = new long[k];
                for (int a = 0; a < k; a++) {
                    if (cur0[a] == 0) continue;
                    for (int b = 0; b < k; b++) {
                        if (tot[b] == 0) continue;
                        nxt0[(a + b) % k] = (nxt0[(a + b) % k] + cur0[a] * tot[b]) % MOD;
                    }
                }
                cur0 = nxt0;
                var nxt1 = new long[k];
                for (int a = 0; a < k; a++) {
                    if (cur1[a] == 0) continue;
                    for (int b = 0; b < k; b++) {
                        if (dp0[ch][b] == 0) continue;
                        nxt1[(a + b) % k] = (nxt1[(a + b) % k] + cur1[a] * dp0[ch][b]) % MOD;
                    }
                }
                cur1 = nxt1;
            }
            dp0[u] = cur0;
            dp1[u] = cur1;
        }
        return (int)((dp0[0][0] + dp1[0][0] - 1) % MOD);
    }
}
