// LeetCode 1981. Minimize the Difference Between Target and Chosen Elements — Medium
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/
// Submission 2204092531 — Accepted, C#

// My thinking: I must pick exactly one number from each row, so the only
// thing that matters after processing some rows is which totals I can
// reach. I keep a True/False table over all reachable sums: I start with
// only sum 0 reachable, and for each new row I mark every old sum plus
// each number in that row as reachable. The biggest possible total is the
// sum of the largest number in each row, so the table stays small (at most
// 70 rows times 70 per number). Once every row is processed, I scan the
// reachable sums and return the smallest distance from the target.
public class Solution {
    public int MinimizeTheDifference(int[][] mat, int target) {
        int maxSum = 0;
        foreach (int[] row in mat) {
            int rowMax = row[0];
            foreach (int x in row) rowMax = Math.Max(rowMax, x);
            maxSum += rowMax;
        }
        bool[] dp = new bool[maxSum + 1];
        dp[0] = true;
        foreach (int[] row in mat) {
            bool[] ndp = new bool[maxSum + 1];
            for (int s = 0; s <= maxSum; s++) {
                if (dp[s]) {
                    foreach (int x in row) {
                        ndp[s + x] = true;
                    }
                }
            }
            dp = ndp;
        }
        int ans = int.MaxValue;
        for (int s = 0; s <= maxSum; s++) {
            if (dp[s]) ans = Math.Min(ans, Math.Abs(s - target));
        }
        return ans;
    }
}
