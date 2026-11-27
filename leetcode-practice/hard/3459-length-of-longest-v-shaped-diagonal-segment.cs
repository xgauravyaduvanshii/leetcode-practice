// LeetCode 3459. Length of Longest V-Shaped Diagonal Segment — Hard
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/
// Submission 2202556244 — Accepted 561/561, C#
public class Solution {
    public int LenOfVDiagonal(int[][] grid) {
        // My thinking: the values after the starting 1 must run
        // 2, 0, 2, 0, ..., so from any cell the next value is
        // forced by the current one — no step parity needs
        // storing. I first tabulate, per diagonal direction,
        // the straight alternating run from each cell. Then,
        // per direction, a second table adds the best option of
        // going straight or turning once clockwise, both read
        // from tables already filled by walking each diagonal
        // backwards.
        int n = grid.Length;
        int m = grid[0].Length;
        // Clockwise diagonal order: SE, SW, NW, NE, so a turn
        // is (d + 1) % 4.
        int[,] dirs = { { 1, 1 }, { 1, -1 }, { -1, -1 }, { -1, 1 } };

        // g[d, i, j]: straight alternating run starting at
        // (i, j) in direction d (0 unless grid is 0 or 2).
        int[,,] g = new int[4, n, m];
        for (int d = 0; d < 4; d++) {
            int di = dirs[d, 0], dj = dirs[d, 1];
            for (int ii = 0; ii < n; ii++) {
                int i = di == 1 ? n - 1 - ii : ii;
                for (int jj = 0; jj < m; jj++) {
                    int j = dj == 1 ? m - 1 - jj : jj;
                    int v = grid[i][j];
                    if (v != 0 && v != 2) continue;
                    int ni = i + di, nj = j + dj;
                    int nxt = v == 2 ? 0 : 2;
                    if (ni >= 0 && ni < n && nj >= 0 && nj < m && grid[ni][nj] == nxt)
                        g[d, i, j] = 1 + g[d, ni, nj];
                    else
                        g[d, i, j] = 1;
                }
            }
        }

        int ans = 0;
        for (int d = 0; d < 4; d++) {
            int di = dirs[d, 0], dj = dirs[d, 1];
            int td = (d + 1) % 4;
            int tdi = dirs[td, 0], tdj = dirs[td, 1];
            // f: same as g, but the one clockwise turn is still
            // available from each cell.
            int[,] f = new int[n, m];
            for (int ii = 0; ii < n; ii++) {
                int i = di == 1 ? n - 1 - ii : ii;
                for (int jj = 0; jj < m; jj++) {
                    int j = dj == 1 ? m - 1 - jj : jj;
                    int v = grid[i][j];
                    if (v != 0 && v != 2) continue;
                    int nxt = v == 2 ? 0 : 2;
                    int best = 0;
                    int ni = i + di, nj = j + dj;
                    if (ni >= 0 && ni < n && nj >= 0 && nj < m && grid[ni][nj] == nxt)
                        best = f[ni, nj];
                    int mi = i + tdi, mj = j + tdj;
                    if (mi >= 0 && mi < n && mj >= 0 && mj < m && grid[mi][mj] == nxt)
                        best = Math.Max(best, g[td, mi, mj]);
                    f[i, j] = 1 + best;
                }
            }
            // Start from every 1 and step into direction d.
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (grid[i][j] != 1) continue;
                    int ni = i + di, nj = j + dj;
                    int length = 1;
                    if (ni >= 0 && ni < n && nj >= 0 && nj < m && grid[ni][nj] == 2)
                        length += f[ni, nj];
                    ans = Math.Max(ans, length);
                }
            }
        }
        return ans;
    }
}
