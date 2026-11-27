// LeetCode 3869. Count Fancy Numbers in a Range — Hard
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/
// Submission 2203329478 — Accepted, C#
using System;

public class Solution {
    private int[] digits;
    private long[,,,,,] memo;
    private bool[,,,,,] seen;

    // True when the decimal digits of x are strictly
    // monotone; a single digit is good by definition.
    private bool IsGoodSum(int x) {
        int[] ds = new int[4];
        int len = 0;
        if (x == 0) {
            ds[len++] = 0;
        } else {
            while (x > 0) {
                ds[len++] = x % 10;
                x /= 10;
            }
        }
        // ds holds the digits reversed; strict monotonicity
        // is the same either way round.
        bool inc = true, dec = true;
        for (int i = 0; i + 1 < len; i++) {
            if (ds[i] >= ds[i + 1]) inc = false;
            if (ds[i] <= ds[i + 1]) dec = false;
        }
        return inc || dec;
    }

    // Digit DP over the digits of n. direction: 0 undecided
    // (fewer than two digits placed), 1 increasing,
    // 2 decreasing, 3 already not strictly monotone.
    private long Dfs(int pos, int tight, int started, int last, int dir, int sum) {
        if (pos == digits.Length) {
            if (started == 0) return 0;
            if (dir != 3) return 1;
            return IsGoodSum(sum) ? 1 : 0;
        }
        if (seen[pos, tight, started, last, dir, sum]) return memo[pos, tight, started, last, dir, sum];
        seen[pos, tight, started, last, dir, sum] = true;
        long res = 0;
        int limit = tight == 1 ? digits[pos] : 9;
        for (int d = 0; d <= limit; d++) {
            int ntight = (tight == 1 && d == limit) ? 1 : 0;
            if (started == 0 && d == 0) {
                res += Dfs(pos + 1, ntight, 0, 0, 0, sum);
            } else {
                int ndir;
                if (started == 0) ndir = 0;
                else if (dir == 3) ndir = 3;
                else if (dir == 0) ndir = d > last ? 1 : d < last ? 2 : 3;
                else if (dir == 1) ndir = d > last ? 1 : 3;
                else ndir = d < last ? 2 : 3;
                res += Dfs(pos + 1, ntight, 1, d, ndir, sum + d);
            }
        }
        memo[pos, tight, started, last, dir, sum] = res;
        return res;
    }

    private long CountUpTo(long n) {
        if (n <= 0) return 0;
        string s = n.ToString();
        digits = new int[s.Length];
        for (int i = 0; i < s.Length; i++) digits[i] = s[i] - '0';
        // Digit sums reach at most 9 * 16 = 144.
        memo = new long[17, 2, 2, 10, 4, 146];
        seen = new bool[17, 2, 2, 10, 4, 146];
        return Dfs(0, 1, 0, 0, 0, 0);
    }

    public long CountFancy(long l, long r) {
        // My thinking: count fancy numbers up to n with a
        // digit DP, then answer F(r) - F(l - 1). The DP walks
        // the decimal digits of n tracking tight, whether a
        // digit has started, the last digit placed, the
        // direction of the digits so far (undecided,
        // increasing, decreasing, or already broken) and the
        // digit sum, which is at most 9 * 16 = 144. At the
        // end a number is fancy when its digits stayed
        // strictly monotone, or when its digit sum — itself
        // a one-to-three-digit number — is good. Leading
        // zeros never start the number, so 0 is not counted.
        return CountUpTo(r) - CountUpTo(l - 1);
    }
}
