// LeetCode 2028. Find Missing Observations — Medium
// https://leetcode.com/problems/find-missing-observations/
// Submission 2204148631 — Accepted, C#

// My thinking: the missing rolls have to add up to a fixed
// total — mean times all n + m rolls, minus the rolls I can
// still see. If that total is less than n (every missing roll
// is at least 1) or more than 6 * n (every missing roll is at
// most 6), no answer exists and I return an empty array.
// Otherwise I spread the total as evenly as possible: every
// missing roll gets total / n, and the leftover remainder
// adds one extra to that many rolls, so each value stays
// between 1 and 6.
public class Solution {
    public int[] MissingRolls(int[] rolls, int mean, int n) {
        int missingTotal = mean * (rolls.Length + n) - rolls.Sum();
        if (missingTotal < n || missingTotal > 6 * n) {
            return new int[0];
        }
        int baseValue = missingTotal / n;
        int extra = missingTotal % n;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = baseValue + (i < extra ? 1 : 0);
        }
        return ans;
    }
}
