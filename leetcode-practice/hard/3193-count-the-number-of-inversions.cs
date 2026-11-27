// LeetCode 3193. Count the Number of Inversions — Hard
// https://leetcode.com/problems/count-the-number-of-inversions/
// Submission 2202074276 — Accepted, C#
//
// My thinking: I build permutations one
// element at a time: inserting the new
// largest element into a permutation of
// length L adds anywhere from 0 to L-1
// inversions, so the counts follow a
// sliding-window DP over inversion
// totals, kept in prefix sums. Whenever
// a requirement pins the count at some
// length, I zero out every other count
// and continue.

public class Solution {
    public int NumberOfPermutations(int n, int[][] requirements) {
        const int MOD = 1000000007;
        const int MAXC = 400;
        var req = new Dictionary<int, int>();
        foreach (var r in requirements) req[r[0]] = r[1];
        long[] dp = new long[MAXC + 1];
        dp[0] = 1;
        for (int length = 1; length <= n; length++) {
            long[] pref = new long[MAXC + 1];
            long s = 0;
            for (int j = 0; j <= MAXC; j++) {
                s = (s + dp[j]) % MOD;
                pref[j] = s;
            }
            long[] ndp = new long[MAXC + 1];
            for (int j = 0; j <= MAXC; j++) {
                long val = pref[j];
                if (j - length >= 0) val -= pref[j - length];
                ndp[j] = (val % MOD + MOD) % MOD;
            }
            if (req.ContainsKey(length - 1)) {
                int cnt = req[length - 1];
                long keep = cnt <= MAXC ? ndp[cnt] : 0;
                ndp = new long[MAXC + 1];
                if (cnt <= MAXC) ndp[cnt] = keep;
            }
            dp = ndp;
        }
        return (int)(dp[req[n - 1]] % MOD);
    }
}
