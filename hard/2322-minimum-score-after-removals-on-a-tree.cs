// LeetCode 2322. Minimum Score After Removals on a Tree — Hard
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
// Submission 2201678500 — Accepted, C#
//
// My thinking: cutting two edges leaves
// three pieces, and each piece is either a
// whole subtree or what is left of one — so
// I root the tree, take every subtree's
// xor, and try every pair of cuts.

using System;
using System.Collections.Generic;

public class Solution {
    private List<int>[] adj;
    private int[] sub;
    private int[] tin;
    private int[] tout;
    private int timer;

    public int MinimumScore(int[] nums, int[][] edges) {
        int n = nums.Length;
        adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            adj[e[0]].Add(e[1]);
            adj[e[1]].Add(e[0]);
        }
        sub = new int[n];
        tin = new int[n];
        tout = new int[n];
        timer = 0;
        int total = Dfs(0, -1, nums);
        int ans = int.MaxValue;
        for (int u = 1; u < n; u++) {
            for (int v = u + 1; v < n; v++) {
                int a, b, c;
                if (IsAncestor(u, v)) {
                    a = sub[v]; b = sub[u] ^ sub[v]; c = total ^ sub[u];
                } else if (IsAncestor(v, u)) {
                    a = sub[u]; b = sub[v] ^ sub[u]; c = total ^ sub[v];
                } else {
                    a = sub[u]; b = sub[v]; c = total ^ sub[u] ^ sub[v];
                }
                int score = Math.Max(Math.Max(a, b), c) - Math.Min(Math.Min(a, b), c);
                ans = Math.Min(ans, score);
            }
        }
        return ans;
    }

    private int Dfs(int u, int p, int[] nums) {
        tin[u] = timer++;
        int x = nums[u];
        foreach (int v in adj[u]) {
            if (v != p) x ^= Dfs(v, u, nums);
        }
        sub[u] = x;
        tout[u] = timer++;
        return x;
    }

    private bool IsAncestor(int u, int v) {
        return tin[u] <= tin[v] && tout[v] <= tout[u];
    }
}
