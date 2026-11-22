// LeetCode 1761. Minimum Degree of a Connected Trio in a Graph — Hard
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
// Submission 2201149077 — Accepted, C#
//
// My thinking: every trio sits on one of its three
// edges, so for each edge I look at the neighbours
// both ends share — each shared neighbour closes a
// trio, and its degree is the three degrees added
// up minus the six edges inside the trio.

using System;
using System.Collections.Generic;

public class Solution {
    public int MinTrioDegree(int n, int[][] edges) {
        var adj = new HashSet<int>[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new HashSet<int>();
        foreach (var e in edges) {
            adj[e[0]].Add(e[1]);
            adj[e[1]].Add(e[0]);
        }
        int best = int.MaxValue;
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            foreach (int w in adj[u]) {
                if (adj[v].Contains(w)) {
                    int deg = adj[u].Count + adj[v].Count + adj[w].Count - 6;
                    if (deg < best) best = deg;
                }
            }
        }
        return best == int.MaxValue ? -1 : best;
    }
}
