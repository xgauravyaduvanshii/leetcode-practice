// LeetCode 3149. Find the Minimum Cost Array Permutation — Hard
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/
// Submission 2202041780 — Accepted, C#
//
// My thinking: the cost of a permutation
// is a tour starting at 0, so I run a
// Held-Karp DP over subsets: f[mask][last]
// is the cheapest cost of visiting exactly
// the set mask and ending at last. A second
// DP walks backwards from the full set to
// rebuild the cheapest tour greedily,
// always picking the smallest next step
// that can still reach the optimum.

public class Solution {
    public int[] FindPermutation(int[] nums) {
        int n = nums.Length;
        int N = 1 << n;
        const int INF = 1000000000;
        int[,] cost = new int[n, n];
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) {
                cost[a, b] = System.Math.Abs(a - nums[b]);
            }
        }
        int[,] f = new int[N, n];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < n; j++) {
                f[i, j] = INF;
            }
        }
        f[1, 0] = 0;
        for (int mask = 0; mask < N; mask++) {
            if ((mask & 1) == 0) continue;
            for (int last = 0; last < n; last++) {
                int cur = f[mask, last];
                if (cur == INF) continue;
                for (int nxt = 0; nxt < n; nxt++) {
                    if ((mask & (1 << nxt)) != 0) continue;
                    int nmask = mask | (1 << nxt);
                    int val = cur + cost[last, nxt];
                    if (val < f[nmask, nxt]) f[nmask, nxt] = val;
                }
            }
        }
        int full = N - 1;
        int opt = INF;
        for (int last = 0; last < n; last++) {
            opt = System.Math.Min(opt, f[full, last] + cost[last, 0]);
        }
        int[,] g = new int[N, n];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < n; j++) {
                g[i, j] = INF;
            }
        }
        for (int last = 0; last < n; last++) {
            g[full, last] = cost[last, 0];
        }
        for (int mask = N - 1; mask >= 0; mask--) {
            if ((mask & 1) == 0 || mask == full) continue;
            for (int last = 0; last < n; last++) {
                if ((mask & (1 << last)) == 0) continue;
                int best = INF;
                for (int nxt = 0; nxt < n; nxt++) {
                    if ((mask & (1 << nxt)) != 0) continue;
                    int cand = cost[last, nxt] + g[mask | (1 << nxt), nxt];
                    if (cand < best) best = cand;
                }
                g[mask, last] = best;
            }
        }
        int[] perm = new int[n];
        perm[0] = 0;
        int idx = 1;
        int cmask = 1;
        int clast = 0;
        int spent = 0;
        while (cmask != full) {
            for (int nxt = 0; nxt < n; nxt++) {
                if ((cmask & (1 << nxt)) != 0) continue;
                if (spent + cost[clast, nxt] + g[cmask | (1 << nxt), nxt] == opt) {
                    perm[idx++] = nxt;
                    spent += cost[clast, nxt];
                    cmask |= (1 << nxt);
                    clast = nxt;
                    break;
                }
            }
        }
        return perm;
    }
}
