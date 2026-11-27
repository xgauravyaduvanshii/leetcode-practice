// LeetCode 3981. Count Distinct Ways to Form Target from Two Strings — Hard
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/
// Submission 2203496047 — Accepted, Java
class Solution {
    private static final int MOD = 1000000007;

    public int interleaveCharacters(String word1, String word2, String target) {
        // My thinking: work backwards through the target.
        // f(i, j, t) is the number of ways to form
        // target[t:] using word1[i:] and word2[j:]; its
        // first character comes from word1 at some position
        // p >= i or from word2 at some position q >= j,
        // and suffix sums over p and q make each level
        // O(n^2). The empty suffix has one way. This counts
        // every way, including ones that use only one word,
        // so subtract the plain subsequence counts of the
        // target in each word alone; the two subtracted sets
        // are disjoint. Everything is modulo 10^9 + 7.
        int n1 = word1.length();
        int n2 = word2.length();
        int m = target.length();
        int[][] nxt = new int[n1 + 1][n2 + 1];
        for (int i = 0; i <= n1; i++) {
            for (int j = 0; j <= n2; j++) nxt[i][j] = 1;
        }
        for (int t = m - 1; t >= 0; t--) {
            char ch = target.charAt(t);
            int[][] s1 = new int[n1 + 2][n2 + 1];
            int[][] s2 = new int[n1 + 1][n2 + 2];
            for (int i = n1; i >= 0; i--) {
                for (int j = 0; j <= n2; j++) {
                    int add = (i < n1 && word1.charAt(i) == ch) ? nxt[i + 1][j] : 0;
                    s1[i][j] = (s1[i + 1][j] + add) % MOD;
                }
            }
            for (int i = 0; i <= n1; i++) {
                for (int j = n2; j >= 0; j--) {
                    int add = (j < n2 && word2.charAt(j) == ch) ? nxt[i][j + 1] : 0;
                    s2[i][j] = (s2[i][j + 1] + add) % MOD;
                }
            }
            int[][] cur = new int[n1 + 1][n2 + 1];
            for (int i = 0; i <= n1; i++) {
                for (int j = 0; j <= n2; j++) {
                    cur[i][j] = (s1[i][j] + s2[i][j]) % MOD;
                }
            }
            nxt = cur;
        }
        int total = nxt[0][0];
        int ans = (total - subseqCount(word1, target, m) - subseqCount(word2, target, m)) % MOD;
        return ans < 0 ? ans + MOD : ans;
    }

    private int subseqCount(String w, String target, int m) {
        int[] dp = new int[m + 1];
        dp[0] = 1;
        for (int i = 0; i < w.length(); i++) {
            char ch = w.charAt(i);
            for (int t = m; t >= 1; t--) {
                if (ch == target.charAt(t - 1)) {
                    dp[t] = (dp[t] + dp[t - 1]) % MOD;
                }
            }
        }
        return dp[m];
    }
}
