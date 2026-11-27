// LeetCode 3600. Maximize Spanning Tree Stability with Upgrades — Hard
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
// Submission 2202866832 — Accepted, C#
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxStability(int n, int[][] edges, int k) {
        // My thinking: first the must-edges have to be acyclic, and
        // the graph as a whole has to be connected, or the answer is
        // -1. For a target stability X, a must-edge is usable only
        // at its own strength, an optional edge is free when its
        // strength already reaches X and costs one upgrade when
        // doubling it does. I take the free edges first, then the
        // cheapest upgraded ones, and X works when the tree closes
        // with at most k upgrades. That test is monotone in X, so I
        // binary search the largest working X.
        var must = new List<int[]>();
        var opt = new List<int[]>();
        foreach (var e in edges) {
            if (e[3] == 1) must.Add(e);
            else opt.Add(e);
        }
        var dsu = new DSU(n);
        foreach (var e in must) {
            if (!dsu.Union(e[0], e[1])) return -1;
        }
        var dsu2 = new DSU(n);
        int comps = n;
        foreach (var e in edges) {
            if (dsu2.Union(e[0], e[1])) comps--;
        }
        if (comps > 1) return -1;
        int lo = 1, hi = 200001, best = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (Feasible(n, must, opt, k, mid)) {
                best = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return best;
    }

    private static bool Feasible(int n, List<int[]> must, List<int[]> opt, int k, int X) {
        var dsu = new DSU(n);
        foreach (var e in must) {
            if (e[2] < X) return false;
            dsu.Union(e[0], e[1]);
        }
        int used = 0, upgrades = 0;
        foreach (var e in opt) {
            if (e[2] >= X && dsu.Find(e[0]) != dsu.Find(e[1])) {
                dsu.Union(e[0], e[1]);
                used++;
            }
        }
        foreach (var e in opt) {
            if (e[2] < X && 2 * e[2] >= X && dsu.Find(e[0]) != dsu.Find(e[1])) {
                dsu.Union(e[0], e[1]);
                upgrades++;
                used++;
            }
        }
        int need = (n - 1) - must.Count;
        if (used < need || upgrades > k) return false;
        int root = dsu.Find(0);
        for (int i = 1; i < n; i++) {
            if (dsu.Find(i) != root) return false;
        }
        return true;
    }

    private class DSU {
        private int[] parent;
        private int[] rank;
        public DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        public int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        public bool Union(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra == rb) return false;
            if (rank[ra] < rank[rb]) { int t = ra; ra = rb; rb = t; }
            parent[rb] = ra;
            if (rank[ra] == rank[rb]) rank[ra]++;
            return true;
        }
    }
}
