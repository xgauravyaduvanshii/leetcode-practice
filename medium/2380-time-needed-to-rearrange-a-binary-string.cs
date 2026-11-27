// LeetCode 2380. Time Needed to Rearrange a Binary String — Medium
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
// Submission 2204769354 — Accepted, C#
//
// My thinking: same idea as the Python version — each '1' needs at
// least as many seconds as there are zeros before it, and one second
// more than the previous '1' needed; the max over all '1's is the
// answer.
public class Solution {
    public int SecondsToRemoveOccurrences(string s) {
        int seconds = 0;
        int zeros = 0;
        foreach (char ch in s) {
            if (ch == '0') {
                zeros++;
            } else if (zeros > 0) {
                seconds = System.Math.Max(seconds + 1, zeros);
            }
        }
        return seconds;
    }
}
