// LeetCode 1977. Number of Ways to Separate Numbers — Hard
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/
// Submission 2201285485 — Accepted, Java
//
// My thinking: the numbers are all positive, so
// no number may start with 0 — not even a lone
// 0. Two numbers compare by length first, then
// by their first differing digit, so I precompute
// longest common prefixes and count the splits
// with a prefix-summed table.

class Solution {
    private static final int MOD = 1_000_000_007;

    public int numberOfCombinations(String num) {
        int n = num.length();
        if (num.charAt(0) == '0') return 0;
        int[][] lcp = new int[n + 1][n + 1];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (num.charAt(i) == num.charAt(j)) {
                    lcp[i][j] = lcp[i + 1][j + 1] + 1;
                }
            }
        }
        int[][] dp = new int[n + 1][n + 1];
        int[][] pre = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i][0] = 1;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                if (num.charAt(j) == '0') continue;
                int lo = 2 * j - i + 1;
                if (lo < 0) lo = 0;
                long total = 0;
                if (lo <= j - 1) {
                    total = (pre[j][j - 1] - (lo > 0 ? pre[j][lo - 1] : 0)) % MOD;
                }
                int k0 = 2 * j - i;
                if (k0 >= 0 && k0 < j) {
                    int len = j - k0;
                    int common = lcp[k0][j];
                    boolean le = common >= len || num.charAt(k0 + common) < num.charAt(j + common);
                    if (le) total = (total + dp[j][k0]) % MOD;
                }
                dp[i][j] = (int) ((total % MOD + MOD) % MOD);
            }
            long s = 0;
            for (int k = 0; k < i; k++) {
                s = (s + dp[i][k]) % MOD;
                pre[i][k] = (int) s;
            }
        }
        long ans = 0;
        for (int j = 0; j < n; j++) ans = (ans + dp[n][j]) % MOD;
        return (int) ans;
    }
}
