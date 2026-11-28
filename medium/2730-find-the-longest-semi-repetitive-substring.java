// LeetCode 2730. Find the Longest Semi-Repetitive Substring — Medium
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/
// Submission 2205214214 — Accepted, Java
//
// My thinking: same idea as the Python version — a sliding
// window holding at most one adjacent equal pair, shrinking
// from the left whenever a second pair enters.
class Solution {
    public int longestSemiRepetitiveSubstring(String s) {
        int n = s.length();
        int ans = 1, left = 0, pairs = 0;
        for (int right = 1; right < n; right++) {
            if (s.charAt(right) == s.charAt(right - 1)) pairs++;
            while (pairs > 1) {
                if (s.charAt(left) == s.charAt(left + 1)) pairs--;
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
