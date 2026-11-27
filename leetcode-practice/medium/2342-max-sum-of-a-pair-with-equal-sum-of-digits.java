// LeetCode 2342. Max Sum of a Pair With Equal Sum of Digits — Medium
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
// Submission 2204714508 — Accepted, Java
//
// My thinking: same idea as the Python version — keep the biggest number
// seen for each digit sum (an array of size 82 covers every possible
// digit sum) and pair each new number with its group's best.
class Solution {
    public int maximumSum(int[] nums) {
        int[] best = new int[82];
        java.util.Arrays.fill(best, -1);
        int ans = -1;
        for (int v : nums) {
            int d = 0;
            int x = v;
            while (x > 0) {
                d += x % 10;
                x /= 10;
            }
            if (best[d] != -1) {
                ans = Math.max(ans, best[d] + v);
                best[d] = Math.max(best[d], v);
            } else {
                best[d] = v;
            }
        }
        return ans;
    }
}
