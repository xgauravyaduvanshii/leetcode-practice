// LeetCode 3971. Maximum Total Value — Hard
// https://leetcode.com/problems/maximum-total-value/
// Submission 2203491266 — Accepted, C#
using System;
using System.Numerics;

public class Solution {
    private int[] value;
    private int[] decay;

    // Number of gains of at least x over all indices.
    private long CountAtLeast(long x) {
        long total = 0;
        for (int i = 0; i < value.Length; i++) {
            if (value[i] >= x) {
                total += (value[i] - x) / decay[i] + 1;
            }
        }
        return total;
    }

    // Sum of all gains of at least x over all indices,
    // using the arithmetic-series formula per index.
    private BigInteger SumAtLeast(long x) {
        BigInteger total = 0;
        for (int i = 0; i < value.Length; i++) {
            if (value[i] >= x) {
                long c = (value[i] - x) / decay[i] + 1;
                total += (BigInteger)c * value[i] - (BigInteger)decay[i] * c * (c - 1) / 2;
            }
        }
        return total;
    }

    public int MaxTotalValue(int[] value, int[] decay, int m) {
        // My thinking: every selection is one gain from the
        // arithmetic sequences value[i], value[i]-decay[i],
        // ... while they stay positive, and the best m
        // selections are simply the m largest gains. For a
        // threshold x, the count of gains of at least x and
        // their sum both follow from the arithmetic-series
        // formula, and both are monotone in x, so binary
        // search finds the largest threshold T whose count
        // reaches the number taken; then take every gain
        // above T and fill the rest with gains equal to T.
        // Only positive gains are ever taken. The sums can
        // reach about 10^27, so they are kept in BigInteger
        // and reduced modulo 10^9 + 7 only at the end.
        this.value = value;
        this.decay = decay;
        const long MOD = 1000000007;
        long take = Math.Min((long)m, CountAtLeast(1));
        if (take == 0) return 0;
        long lo = 1, hi = 0;
        foreach (int v in value) hi = Math.Max(hi, v);
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (CountAtLeast(mid) >= take) lo = mid;
            else hi = mid - 1;
        }
        BigInteger total = SumAtLeast(lo + 1) + (BigInteger)(take - CountAtLeast(lo + 1)) * lo;
        return (int)(total % MOD);
    }
}
