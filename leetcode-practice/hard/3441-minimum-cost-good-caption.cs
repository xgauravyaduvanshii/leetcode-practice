// LeetCode 3441. Minimum Cost Good Caption — Hard
// https://leetcode.com/problems/minimum-cost-good-caption/
// Submission 2202537824 — Accepted 714/714, C#
public class Solution {
    public string MinCostGoodCaption(string caption) {
        // My thinking: a good caption is runs of one letter, each at least
        // 3 long, so I work backwards: for every position and every letter
        // the run ending just before it could have, I keep the cheapest
        // cost of finishing the rest. A new run may only start once the
        // previous run reached length 3. Then I walk forward, always taking
        // the smallest letter that can still reach the cheapest total —
        // that gives the lexicographically smallest cheapest caption.
        int n = caption.Length;
        if (n < 3) return "";
        int[] cap = new int[n];
        for (int i = 0; i < n; i++) cap[i] = caption[i] - 'a';
        const int INF = 1000000000;
        // h1/h2/h3[i][c]: cheapest cost of caption[i..] when the run ending
        // at i-1 has letter c and length 1 / 2 / at least 3.
        int[][] h1 = new int[n + 1][];
        int[][] h2 = new int[n + 1][];
        int[][] h3 = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            h1[i] = new int[26];
            h2[i] = new int[26];
            h3[i] = new int[26];
            for (int c = 0; c < 26; c++) {
                h1[i][c] = INF;
                h2[i][c] = INF;
                h3[i][c] = 0;
            }
        }
        int[] A = new int[26];
        for (int i = n - 1; i >= 0; i--) {
            int ci = cap[i];
            for (int d = 0; d < 26; d++) A[d] = Math.Abs(ci - d) + h1[i + 1][d];
            int b1 = INF, b2 = INF, c1 = -1;
            for (int d = 0; d < 26; d++) {
                int v = A[d];
                if (v < b1) {
                    b2 = b1;
                    b1 = v;
                    c1 = d;
                } else if (v < b2) {
                    b2 = v;
                }
            }
            for (int c = 0; c < 26; c++) {
                int cost = Math.Abs(ci - c);
                int bestNew = (c1 != c) ? b1 : b2;
                h3[i][c] = Math.Min(cost + h3[i + 1][c], bestNew);
                h2[i][c] = cost + h3[i + 1][c];
                h1[i][c] = cost + h2[i + 1][c];
            }
        }
        int total = INF;
        for (int d = 0; d < 26; d++) {
            total = Math.Min(total, Math.Abs(cap[0] - d) + h1[1][d]);
        }
        char[] res = new char[n];
        int prev = -1, run = 0, remaining = total;
        for (int i = 0; i < n; i++) {
            int ci = cap[i];
            for (int d = 0; d < 26; d++) {
                int cost = Math.Abs(ci - d);
                int value, newRun;
                if (prev == -1) {
                    value = cost + h1[i + 1][d];
                    newRun = 1;
                } else if (d == prev) {
                    int nr = run == 3 ? 3 : run + 1;
                    value = cost + (nr == 3 ? h3[i + 1][d] : nr == 2 ? h2[i + 1][d] : h1[i + 1][d]);
                    newRun = nr;
                } else if (run == 3) {
                    value = cost + h1[i + 1][d];
                    newRun = 1;
                } else {
                    continue;
                }
                if (value == remaining) {
                    res[i] = (char)('a' + d);
                    remaining -= cost;
                    prev = d;
                    run = newRun;
                    break;
                }
            }
        }
        return new string(res);
    }
}
