// LeetCode 2745. Construct the Longest New String — Medium
// https://leetcode.com/problems/construct-the-longest-new-string/
// Submission 2205233132 — Accepted, C#
//
// My thinking: same idea as the Python version — "AA" and "BB"
// blocks alternate for 2*min(x, y) blocks, one extra block of
// the majority kind fits when x != y, and all z "AB" blocks fit
// together at one end; each block is 2 letters.
public class Solution {
    public int LongestString(int x, int y, int z) {
        return 2 * (2 * Math.Min(x, y) + z + (x != y ? 1 : 0));
    }
}
