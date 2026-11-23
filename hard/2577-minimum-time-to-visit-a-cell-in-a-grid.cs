// LeetCode 2577. Minimum Time to Visit a Cell In a Grid — Hard
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
// Submission 2201830519 — Accepted, C#
//
// My thinking: every step flips the
// parity of where I stand, so the
// earliest I can enter a cell is its
// opening time rounded up to my parity
// — I let Dijkstra carry the earliest
// arrival everywhere, and if both doors
// out of the start open too late there
// is no way in at all.

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumTime(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        if (m == 1 && n == 1) return 0;
        // you must leave the start at t = 1; if every neighbour opens later,
        // there is nowhere to go and no way to wait
        bool stuck = true;
        int[][] dirs = new int[][] {
            new int[] {1, 0}, new int[] {-1, 0}, new int[] {0, 1}, new int[] {0, -1}
        };
        foreach (var d in dirs) {
            int nr = d[0], nc = d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] <= 1) {
                stuck = false;
                break;
            }
        }
        if (stuck) return -1;
        const int INF = int.MaxValue;
        int[,] dist = new int[m, n];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                dist[r, c] = INF;
        dist[0, 0] = 0;
        var pq = new PriorityQueue<(int t, int r, int c), int>();
        pq.Enqueue((0, 0, 0), 0);
        while (pq.Count > 0) {
            var (t, r, c) = pq.Dequeue();
            if (t != dist[r, c]) continue;
            if (r == m - 1 && c == n - 1) return t;
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nt = Math.Max(t + 1, grid[nr][nc]);
                if ((nt - (nr + nc)) % 2 != 0) nt++;
                if (nt < dist[nr, nc]) {
                    dist[nr, nc] = nt;
                    pq.Enqueue((nt, nr, nc), nt);
                }
            }
        }
        return -1;
    }
}
