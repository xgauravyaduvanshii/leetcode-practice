// LeetCode 2360. Longest Cycle in a Graph — Hard
// https://leetcode.com/problems/longest-cycle-in-a-graph/
// Submission 2201698957 — Accepted, C#
//
// My thinking: every node points to at
// most one next node, so I walk each chain
// once, stamping when I first meet a node
// — meeting one again inside the same walk
// is a cycle, and its length is how far I
// have come since that stamp.

using System.Collections.Generic;

public class Solution {
    public int LongestCycle(int[] edges) {
        int n = edges.Length;
        bool[] visited = new bool[n];
        int ans = -1;
        for (int start = 0; start < n; start++) {
            if (visited[start]) continue;
            Dictionary<int, int> step = new Dictionary<int, int>();
            int u = start;
            int s = 0;
            while (u != -1 && !visited[u]) {
                if (step.ContainsKey(u)) {
                    ans = System.Math.Max(ans, s - step[u]);
                    break;
                }
                step[u] = s;
                s++;
                u = edges[u];
            }
            foreach (int node in step.Keys) {
                visited[node] = true;
            }
        }
        return ans;
    }
}
