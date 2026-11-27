// LeetCode 2472. Maximum Number of Non-overlapping Palindrome Substrings — Hard
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
// Submission 2201769451 — Accepted, Java
//
// My thinking: a palindrome I take can
// only end where one starts — I first
// learn which stretches read the same
// backwards, then walk the string once,
// either skipping the next character or
// closing the best palindrome that ends
// here and counting it.

class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        boolean[][] pal = new boolean[n + 1][n + 1];
        for (int i = 0; i < n; i++) pal[i][i + 1] = true;
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len <= n; i++) {
                int j = i + len;
                if (s.charAt(i) == s.charAt(j - 1) && (len <= 2 || pal[i + 1][j - 1])) {
                    pal[i][j] = true;
                }
            }
        }
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1];
            for (int j = 0; j < i; j++) {
                if (i - j >= k && pal[j][i]) dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        return dp[n];
    }
}
