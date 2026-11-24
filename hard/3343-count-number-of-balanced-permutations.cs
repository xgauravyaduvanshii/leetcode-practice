// LeetCode 3343. Count Number of Balanced Permutations — Hard
// https://leetcode.com/problems/count-number-of-balanced-permutations/
// Submission 2202395040 -- Accepted, C#
public class Solution {
    private const int MOD = 1000000007;

    public int CountBalancedPermutations(string num) {
        // My thinking: the digit sum must be even, with half of it on the
        // even positions. I choose which copies of each digit go to the even
        // slots with a DP over digits, tracking how many even slots are
        // filled and their digit sum. To count distinct permutations I weight
        // each choice by 1/k! * 1/(cnt-k)! (the multinomial denominators),
        // then multiply by even! * odd! at the end, which restores the exact
        // count of distinct arrangements of both halves.
        int n = num.Length;
        int total = 0;
        int[] cnt = new int[10];
        foreach (char c in num) {
            int d = c - '0';
            total += d;
            cnt[d]++;
        }
        if (total % 2 != 0) {
            return 0;
        }
        int nEven = (n + 1) / 2;
        int nOdd = n / 2;
        int target = total / 2;
        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        long[] invFact = new long[n + 1];
        invFact[n] = ModPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
        long[,] dp = new long[nEven + 1, target + 1];
        dp[0, 0] = 1;
        for (int d = 0; d < 10; d++) {
            int c = cnt[d];
            if (c == 0) {
                continue;
            }
            long[,] ndp = new long[nEven + 1, target + 1];
            for (int e = 0; e <= nEven; e++) {
                for (int s = 0; s <= target; s++) {
                    long v = dp[e, s];
                    if (v == 0) {
                        continue;
                    }
                    for (int k = 0; k <= System.Math.Min(c, nEven - e); k++) {
                        int ns = s + k * d;
                        if (ns > target) {
                            break;
                        }
                        ndp[e + k, ns] = (ndp[e + k, ns]
                            + v * invFact[k] % MOD * invFact[c - k]) % MOD;
                    }
                }
            }
            dp = ndp;
        }
        return (int)(dp[nEven, target] * fact[nEven] % MOD * fact[nOdd] % MOD);
    }

    private long ModPow(long a, long e) {
        long r = 1;
        while (e > 0) {
            if ((e & 1) == 1) {
                r = r * a % MOD;
            }
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
}
