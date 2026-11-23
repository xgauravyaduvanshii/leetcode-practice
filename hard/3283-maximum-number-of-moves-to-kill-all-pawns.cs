// LeetCode 3283. Maximum Number of Moves to Kill All Pawns — Hard
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/
// Submission 2202179132 — Accepted, C#
//
// My thinking: a knight needs a fixed number of
// moves between any two squares, so I BFS the
// 50x50 board once from each pawn and the king.
// Then it is a game: Alice moves first and
// maximises the total moves, Bob minimises it,
// so I memoise over (captured-mask, last square)
// and pick max on Alice's turns, min on Bob's.

using System;
using System.Collections.Generic;

public class Solution {
    private int n;
    private int[,] dist;
    private int[,] memo;
    private bool[,] seen;
    private int full;

    public int MaxMoves(int kx, int ky, int[][] positions) {
        n = positions.Length;
        int m = n + 1;
        int[,] pts = new int[m, 2];
        pts[0, 0] = kx; pts[0, 1] = ky;
        for (int i = 0; i < n; i++) { pts[i + 1, 0] = positions[i][0]; pts[i + 1, 1] = positions[i][1]; }
        dist = new int[m, m];
        int[,] dirs = {{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};
        for (int s = 0; s < m; s++) {
            int[,] d = new int[50, 50];
            for (int i = 0; i < 50; i++) for (int j = 0; j < 50; j++) d[i, j] = -1;
            var q = new Queue<(int, int)>();
            d[pts[s, 0], pts[s, 1]] = 0;
            q.Enqueue((pts[s, 0], pts[s, 1]));
            while (q.Count > 0) {
                var (x, y) = q.Dequeue();
                for (int k = 0; k < 8; k++) {
                    int nx = x + dirs[k, 0], ny = y + dirs[k, 1];
                    if (nx >= 0 && nx < 50 && ny >= 0 && ny < 50 && d[nx, ny] == -1) {
                        d[nx, ny] = d[x, y] + 1;
                        q.Enqueue((nx, ny));
                    }
                }
            }
            for (int t = 0; t < m; t++) dist[s, t] = d[pts[t, 0], pts[t, 1]];
        }
        full = (1 << n) - 1;
        memo = new int[1 << n, m];
        seen = new bool[1 << n, m];
        return Dp(0, 0);
    }

    private int Dp(int mask, int last) {
        if (mask == full) return 0;
        if (seen[mask, last]) return memo[mask, last];
        seen[mask, last] = true;
        int cnt = 0;
        for (int i = 0; i < n; i++) if (((mask >> i) & 1) == 1) cnt++;
        bool alice = cnt % 2 == 0;
        int best = alice ? int.MinValue / 2 : int.MaxValue / 2;
        for (int i = 0; i < n; i++) if (((mask >> i) & 1) == 0) {
            int val = dist[last, i + 1] + Dp(mask | (1 << i), i + 1);
            if (alice) best = Math.Max(best, val); else best = Math.Min(best, val);
        }
        memo[mask, last] = best;
        return best;
    }
}
