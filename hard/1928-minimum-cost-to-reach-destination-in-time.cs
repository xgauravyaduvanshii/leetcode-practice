// LeetCode 1928. Minimum Cost to Reach Destination in Time — Hard
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
// Submission 2201239321 — Accepted, C#
//
// My thinking: I run Dijkstra ordered by the fee
// paid so far, and for each city I keep only the
// fastest arrival I have actually expanded — a
// slower arrival can never lead to a cheaper trip,
// because the faster one was popped earlier (so it
// also cost no more) and every later fee and time
// from there is the same.

using System;
using System.Collections.Generic;

public class Solution {
    public int MinCost(int maxTime, int[][] edges, int[] passingFees) {
        int n = passingFees.Length;
        var graph = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            graph[e[0]].Add((e[1], e[2]));
            graph[e[1]].Add((e[0], e[2]));
        }
        var best = new int[n];
        for (int i = 0; i < n; i++) best[i] = int.MaxValue;
        var heap = new PriorityQueue<(int, int, int), int>();
        heap.Enqueue((passingFees[0], 0, 0), passingFees[0]);
        while (heap.Count > 0) {
            var (fee, time, u) = heap.Dequeue();
            if (u == n - 1) return fee;
            if (time >= best[u]) continue;
            best[u] = time;
            foreach (var (v, t) in graph[u]) {
                int nt = time + t;
                if (nt <= maxTime) {
                    heap.Enqueue((fee + passingFees[v], nt, v), fee + passingFees[v]);
                }
            }
        }
        return -1;
    }
}
