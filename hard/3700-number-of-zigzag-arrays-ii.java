// LeetCode 3700. Number of ZigZag Arrays II — Hard
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/
// Submission 2203052674 — Accepted, Java
class Solution {
    private static final long MOD = 1000000007L;

    public int zigZagArrays(int n, int l, int r) {
        // My thinking: only the relative order of values matters,
        // so relabel them 0..m-1. Track, for arrays built so far,
        // U[v] = count ending in v with the last step up and
        // D[v] = count ending in v with the last step down. One
        // more step is a prefix sum of D for the new U and a
        // suffix sum of U for the new D, because an up step is
        // only allowed after a down step (and vice versa) — that
        // is exactly what forbids three in a row going the same
        // way. Two steps therefore decouple: U evolves by
        // A = L*R with A[i][j] = min(i, j), D by its mirror
        // image, so I raise A to the needed power with binary
        // exponentiation and finish with at most one extra step.
        int m = r - l + 1;
        // Length-2 arrays: U[v] counts smaller first values, D[v]
        // counts larger first values.
        long[] u0 = new long[m];
        long[] d0 = new long[m];
        for (int i = 0; i < m; i++) {
            u0[i] = i;
            d0[i] = m - 1 - i;
        }
        if (n == 2) {
            long total = 0;
            for (int i = 0; i < m; i++) total = (total + u0[i] + d0[i]) % MOD;
            return (int) total;
        }
        long k = (n - 2) / 2;
        int odd = (n - 2) % 2;
        // A[i][j] = min(i, j).
        long[][] A = new long[m][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                A[i][j] = Math.min(i, j);
            }
        }
        long[][] P = matPow(A, k);
        // W[i] = sum_j P[i][j] * j. U after 2k steps is W, and D
        // after 2k steps is W reversed (mirror symmetry: the
        // down-counts from the top behave like up-counts from
        // the bottom).
        long[] W = new long[m];
        for (int i = 0; i < m; i++) {
            long s = 0;
            for (int j = 0; j < m; j++) {
                s = (s + P[i][j] * j) % MOD;
            }
            W[i] = s;
        }
        long[] U = W;
        long[] D = new long[m];
        for (int i = 0; i < m; i++) D[i] = W[m - 1 - i];
        if (odd == 0) {
            long total = 0;
            for (int i = 0; i < m; i++) total = (total + U[i] + D[i]) % MOD;
            return (int) total;
        }
        // One more step: new U is prefix sums of D, new D is
        // suffix sums of U.
        long newU = 0, run = 0;
        for (int i = 0; i < m; i++) {
            newU = (newU + run) % MOD;
            run = (run + D[i]) % MOD;
        }
        long newD = 0;
        run = 0;
        for (int i = m - 1; i >= 0; i--) {
            newD = (newD + run) % MOD;
            run = (run + U[i]) % MOD;
        }
        return (int) ((newU + newD) % MOD);
    }

    private long[][] matMul(long[][] A, long[][] B) {
        int n = A.length;
        long[][] C = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (A[i][k] == 0) continue;
                for (int j = 0; j < n; j++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    private long[][] matPow(long[][] A, long e) {
        int n = A.length;
        long[][] res = new long[n][n];
        for (int i = 0; i < n; i++) res[i][i] = 1;
        long[][] base = A;
        while (e > 0) {
            if ((e & 1) == 1) res = matMul(res, base);
            base = matMul(base, base);
            e >>= 1;
        }
        return res;
    }
}
