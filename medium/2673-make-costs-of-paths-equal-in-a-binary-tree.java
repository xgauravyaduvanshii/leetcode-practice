// LeetCode 2673. Make Costs of Paths Equal in a Binary Tree — Medium
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/
// Submission 2205189369 — Accepted, Java
//
// My thinking: same idea as the Python version — work bottom-up
// (children have larger indices, so a reverse loop is a valid
// post-order); each internal node pays the gap between its two
// children's best downward paths and passes up its own cost
// plus the larger of the two.
class Solution {
    public int minIncrements(int n, int[] cost) {
        int[] path = new int[n + 1];
        int ans = 0;
        for (int i = n; i >= 1; i--) {
            if (2 * i > n) {
                path[i] = cost[i - 1];
            } else {
                int left = path[2 * i], right = path[2 * i + 1];
                ans += Math.abs(left - right);
                path[i] = cost[i - 1] + Math.max(left, right);
            }
        }
        return ans;
    }
}
