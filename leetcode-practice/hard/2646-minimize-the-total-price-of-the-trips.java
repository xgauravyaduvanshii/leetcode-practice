// LeetCode 2646. Minimize the Total Price of the Trips — Hard
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/
// Submission 2201858034 — Accepted, Java
//
// My thinking: I count how many trips
// cross each node, then halving a node
// saves half its price times its trips
// — and since halved nodes may never sit
// side by side, I pick the best set the
// way you would rob houses on a tree.

import java.util.*;

class Solution {
    public int minimumTotalPrice(int n, int[][] edges, int[] price, int[][] trips) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }
        int[] parent = new int[n];
        int[] depth = new int[n];
        Arrays.fill(parent, -1);
        List<Integer> order = new ArrayList<>();
        parent[0] = -2;
        order.add(0);
        for (int idx = 0; idx < order.size(); idx++) {
            int u = order.get(idx);
            for (int w : adj[u]) {
                if (parent[w] == -1) {
                    parent[w] = u;
                    depth[w] = depth[u] + 1;
                    order.add(w);
                }
            }
        }
        int LOG = 32 - Integer.numberOfLeadingZeros(n);
        int[][] up = new int[LOG][n];
        for (int i = 0; i < n; i++) up[0][i] = parent[i] >= 0 ? parent[i] : i;
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) up[j][i] = up[j - 1][up[j - 1][i]];
        }
        int[] diff = new int[n];
        for (int[] t : trips) {
            int u = t[0], v = t[1];
            int w = lca(u, v, depth, up, parent, LOG);
            diff[u]++;
            diff[v]++;
            diff[w]--;
            if (parent[w] >= 0) diff[parent[w]]--;
        }
        int[] count = new int[n];
        for (int i = order.size() - 1; i >= 0; i--) {
            int u = order.get(i);
            count[u] += diff[u];
            if (parent[u] >= 0) count[parent[u]] += count[u];
        }
        long base = 0;
        for (int i = 0; i < n; i++) base += (long) price[i] * count[i];
        long[] dp0 = new long[n];
        long[] dp1 = new long[n];
        for (int i = order.size() - 1; i >= 0; i--) {
            int u = order.get(i);
            long save = (long) (price[u] / 2) * count[u];
            long s0 = 0, s1 = save;
            for (int w : adj[u]) {
                if (parent[w] == u) {
                    s0 += Math.max(dp0[w], dp1[w]);
                    s1 += dp0[w];
                }
            }
            dp0[u] = s0;
            dp1[u] = s1;
        }
        return (int) (base - Math.max(dp0[0], dp1[0]));
    }

    private int lca(int a, int b, int[] depth, int[][] up, int[] parent, int LOG) {
        if (depth[a] < depth[b]) { int t = a; a = b; b = t; }
        int d = depth[a] - depth[b];
        for (int j = 0; j < LOG; j++) {
            if ((d & (1 << j)) != 0) a = up[j][a];
        }
        if (a == b) return a;
        for (int j = LOG - 1; j >= 0; j--) {
            if (up[j][a] != up[j][b]) {
                a = up[j][a];
                b = up[j][b];
            }
        }
        return parent[a];
    }
}
