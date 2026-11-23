// LeetCode 2617. Minimum Number of Visited Cells in a Grid — Hard
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/
// Submission 2201854712 — Accepted, C#
//
// My thinking: from any cell I can jump
// to every cell still standing in its
// row or column within reach, so I keep
// each row and column as a chain that
// always points at the next unvisited
// cell — every cell is swept up once,
// and the first time the corner is
// reached the count is the smallest.

using System;
using System.Collections.Generic;

public class Solution {
    private int Find(int[] par, int x) {
        while (par[x] != x) {
            par[x] = par[par[x]];
            x = par[x];
        }
        return x;
    }

    public int MinimumVisitedCells(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        if (m == 1 && n == 1) return 1;
        int[][] rowPar = new int[m][];
        for (int i = 0; i < m; i++) {
            rowPar[i] = new int[n + 1];
            for (int c = 0; c <= n; c++) rowPar[i][c] = c;
        }
        int[][] colPar = new int[n][];
        for (int j = 0; j < n; j++) {
            colPar[j] = new int[m + 1];
            for (int r = 0; r <= m; r++) colPar[j][r] = r;
        }
        Action<int, int> remove = (r, c) => {
            rowPar[r][c] = Find(rowPar[r], c + 1);
            colPar[c][r] = Find(colPar[c], r + 1);
        };
        int[,] dist = new int[m, n];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                dist[r, c] = -1;
        dist[0, 0] = 1;
        remove(0, 0);
        var q = new Queue<(int r, int c)>();
        q.Enqueue((0, 0));
        while (q.Count > 0) {
            var (r, c) = q.Dequeue();
            int d = dist[r, c];
            int reach = Math.Min(n - 1, grid[r][c] + c);
            int nc = Find(rowPar[r], c + 1);
            while (nc <= reach) {
                dist[r, nc] = d + 1;
                if (r == m - 1 && nc == n - 1) return d + 1;
                q.Enqueue((r, nc));
                remove(r, nc);
                nc = Find(rowPar[r], nc);
            }
            reach = Math.Min(m - 1, grid[r][c] + r);
            int nr = Find(colPar[c], r + 1);
            while (nr <= reach) {
                dist[nr, c] = d + 1;
                if (nr == m - 1 && c == n - 1) return d + 1;
                q.Enqueue((nr, c));
                remove(nr, c);
                nr = Find(colPar[c], nr);
            }
        }
        return -1;
    }
}
