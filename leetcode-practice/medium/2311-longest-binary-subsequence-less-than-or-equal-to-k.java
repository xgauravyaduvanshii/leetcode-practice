// LeetCode 2311. Longest Binary Subsequence Less Than or Equal to K — Medium
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
// Submission 2204676626 — Accepted, Java
//
// My thinking: same idea as the Python version — take all the '0's for
// free, then scan the '1's from the right and take each one while the
// running value stays <= k, stopping at the first that would break it.
class Solution {
    public int longestSubsequence(String s, int k) {
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') ans++;
        }
        long val = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(s.length() - 1 - i);
            if (ch == '1') {
                if (i >= 30 || val + (1L << i) > k) break;
                val += 1L << i;
                ans++;
            }
        }
        return ans;
    }
}
