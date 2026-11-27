// LeetCode 2359. Find Closest Node to Given Two Nodes — Medium
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
// Submission 2204742579 — Accepted, C#
//
// My thinking: same idea as the Python version — walk the single chain
// from each start node, recording distances, then pick the node on both
// chains minimising the larger distance (smallest index wins ties,
// since I scan in increasing order).
public class Solution {
    public int ClosestMeetingNode(int[] edges, int node1, int node2) {
        int[] d1 = Distances(edges, node1);
        int[] d2 = Distances(edges, node2);
        int ans = -1;
        int best = int.MaxValue;
        for (int v = 0; v < edges.Length; v++) {
            if (d1[v] != -1 && d2[v] != -1) {
                int m = Math.Max(d1[v], d2[v]);
                if (m < best) {
                    best = m;
                    ans = v;
                }
            }
        }
        return ans;
    }

    private int[] Distances(int[] edges, int start) {
        int n = edges.Length;
        int[] dist = new int[n];
        Array.Fill(dist, -1);
        int d = 0;
        int u = start;
        while (u != -1 && dist[u] == -1) {
            dist[u] = d;
            d++;
            u = edges[u];
        }
        return dist;
    }
}
