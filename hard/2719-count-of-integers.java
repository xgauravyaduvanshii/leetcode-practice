// LeetCode 2719. Count of Integers — Hard
// https://leetcode.com/problems/count-of-integers/
// Submission 2201877428 — Accepted, Java
//
// My thinking: counting numbers up to
// a bound by their digit sum is a walk
// down the digits, so I count up to the
// top of the range and subtract the
// count up to just below the bottom —
// the difference is exactly the numbers
// that live between them.

class Solution {
    private static final int MOD = 1_000_000_007;
    private int minSum, maxSum;
    private int[] digits;
    private Long[][][] memo;

    public int count(String num1, String num2, int min_sum, int max_sum) {
        this.minSum = min_sum;
        this.maxSum = max_sum;
        long high = countUpto(num2);
        long low = countUpto(minusOne(num1));
        return (int) ((high - low + MOD) % MOD);
    }

    private long countUpto(String s) {
        digits = new int[s.length()];
        for (int i = 0; i < s.length(); i++) digits[i] = s.charAt(i) - '0';
        memo = new Long[digits.length + 1][2][maxSum + 1];
        return dp(0, 1, 0);
    }

    private long dp(int pos, int tight, int total) {
        if (total > maxSum) return 0;
        if (pos == digits.length) return (total >= minSum && total <= maxSum) ? 1 : 0;
        if (memo[pos][tight][total] != null) return memo[pos][tight][total];
        int limit = tight == 1 ? digits[pos] : 9;
        long ans = 0;
        for (int d = 0; d <= limit; d++) {
            ans += dp(pos + 1, (tight == 1 && d == limit) ? 1 : 0, total + d);
        }
        ans %= MOD;
        memo[pos][tight][total] = ans;
        return ans;
    }

    private String minusOne(String s) {
        char[] ds = s.toCharArray();
        int i = ds.length - 1;
        while (ds[i] == '0') {
            ds[i] = '9';
            i--;
        }
        ds[i]--;
        String t = new String(ds).replaceFirst("^0+", "");
        return t.isEmpty() ? "0" : t;
    }
}
