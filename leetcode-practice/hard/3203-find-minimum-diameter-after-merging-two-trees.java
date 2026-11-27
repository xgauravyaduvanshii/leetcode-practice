// LeetCode 3203. Find Minimum Diameter After Merging Two Trees — Hard
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
// Submission 2202080125 — Accepted, Java
//
// My thinking: merging two trees by one
// edge can only help by joining their
// centres, so the answer is the larger
// of the two diameters and the sum of
// their radii plus one. Each diameter
// comes from two BFS sweeps: the farthest
// node from anywhere is one end of a
// diameter.

import java.util.*;

class Solution {
    public int minimumDiameterAfterMerge(int[][] edges1, int[][] edges2) {
        int d1 = diameter(edges1);
        int d2 = diameter(edges2);
        return Math.max(d1, Math.max(d2, (d1 + 1) / 2 + (d2 + 1) / 2 + 1));
    }
    private int diameter(int[][] edges) {
        int n = edges.length + 1;
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }
        int a = farthest(0, adj, n)[0];
        return farthest(a, adj, n)[1];
    }
    private int[] farthest(int start, List<Integer>[] adj, int n) {
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        dist[start] = 0;
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        dq.add(start);
        int far = start;
        while (!dq.isEmpty()) {
            int u = dq.poll();
            far = u;
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    dq.add(v);
                }
            }
        }
        return new int[]{far, dist[far]};
    }
}
