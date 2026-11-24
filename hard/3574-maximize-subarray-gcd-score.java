// LeetCode 3574. Maximize Subarray GCD Score — Hard
// https://leetcode.com/problems/maximize-subarray-gcd-score/
// Submission 2202853308 — Accepted, Java
class Solution {
    public long maxGCDScore(int[] nums, int k) {
        // My thinking: doubling an element can only raise a
        // subarray's GCD to at most twice its old value, and only
        // when every element holding the smallest power of two gets
        // doubled — the odd part of the GCD never changes. So for
        // each subarray I keep its GCD, the smallest 2-adic
        // valuation inside it, and how many elements sit at that
        // minimum; the score is length times GCD, doubled when that
        // count fits in the budget.
        int n = nums.length;
        int[] v2 = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nums[i], c = 0;
            while (x % 2 == 0) { x /= 2; c++; }
            v2[i] = c;
        }
        long best = 0;
        for (int l = 0; l < n; l++) {
            long g = 0;
            int m = Integer.MAX_VALUE, cnt = 0;
            for (int r = l; r < n; r++) {
                g = gcd(g, nums[r]);
                if (v2[r] < m) { m = v2[r]; cnt = 1; }
                else if (v2[r] == m) { cnt++; }
                long score = (long)(r - l + 1) * g * (cnt <= k ? 2 : 1);
                if (score > best) best = score;
            }
        }
        return best;
    }

    private static long gcd(long a, long b) {
        while (b != 0) { long t = a % b; a = b; b = t; }
        return a;
    }
}
