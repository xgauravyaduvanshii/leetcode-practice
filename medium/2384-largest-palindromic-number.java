// LeetCode 2384. Largest Palindromic Number — Medium
// https://leetcode.com/problems/largest-palindromic-number/
// Submission 2204775306 — Accepted, Java
//
// My thinking: same idea as the Python version — count digits, build
// the left half from the largest digits down using pairs (never starting
// with '0'), take the largest odd-count digit as the middle, mirror the
// half, and answer '0' when nothing is left.
class Solution {
    public String largestPalindromic(String num) {
        int[] cnt = new int[10];
        for (int i = 0; i < num.length(); i++) {
            cnt[num.charAt(i) - '0']++;
        }
        StringBuilder left = new StringBuilder();
        for (int d = 9; d >= 0; d--) {
            int pairs = cnt[d] / 2;
            if (pairs > 0 && (d != 0 || left.length() > 0)) {
                for (int k = 0; k < pairs; k++) {
                    left.append((char) ('0' + d));
                }
            }
        }
        String mid = "";
        for (int d = 9; d >= 0; d--) {
            if (cnt[d] % 2 == 1) {
                mid = String.valueOf((char) ('0' + d));
                break;
            }
        }
        String half = left.toString();
        String ans = half + mid + left.reverse().toString();
        return ans.isEmpty() ? "0" : ans;
    }
}
