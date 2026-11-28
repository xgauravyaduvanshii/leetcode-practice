// LeetCode 2712. Minimum Cost to Make All Characters Equal — Medium
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/
// Submission 2205208335 — Accepted, C#
//
// My thinking: same idea as the Python version — every boundary
// between unequal neighbours must be crossed by a flip, and the
// cheapest crossing is the shorter of the prefix ending there
// and the suffix starting after it.
public class Solution {
    public long MinimumCost(string s) {
        long ans = 0;
        int n = s.Length;
        for (int i = 0; i < n - 1; i++) {
            if (s[i] != s[i + 1]) ans += Math.Min(i + 1, n - i - 1);
        }
        return ans;
    }
}
