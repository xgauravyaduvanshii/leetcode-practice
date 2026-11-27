// LeetCode 120. Triangle — Medium
// https://leetcode.com/problems/triangle/
// Submission 2204015767 — Accepted, C#

// My thinking: I work from the bottom row up. For each number I add the
// cheaper of the two numbers directly below it, because from any spot
// the only moves are down-left and down-right. Reusing one array of the
// running totals keeps the memory down to one row, and once I reach the
// top, the first entry is the cheapest path from the top to the bottom.
public class Solution {
    public int MinimumTotal(IList<IList<int>> triangle) {
        int n = triangle.Count;
        int[] dp = new int[triangle[n - 1].Count];
        for (int i = 0; i < dp.Length; i++) dp[i] = triangle[n - 1][i];
        for (int row = n - 2; row >= 0; row--) {
            for (int i = 0; i < triangle[row].Count; i++) {
                dp[i] = triangle[row][i] + Math.Min(dp[i], dp[i + 1]);
            }
        }
        return dp[0];
    }
}
