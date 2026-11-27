// LeetCode 3806. Maximum Bitwise AND After Increment Operations — Hard
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/
// Submission 2203189131 — Accepted, Java
import java.util.Arrays;

class Solution {
    public int maximumAND(int[] nums, int k, int m) {
        // My thinking: build the answer bit by bit from the top
        // down — a bit can stay set only if m numbers can be
        // raised to values containing all the bits chosen so
        // far, within k increments in total. Raising x to cover
        // a target is cheapest by fixing the lowest missing bit
        // and everything below it: if j is the highest bit where
        // the target has a 1 that x lacks, the cheapest y >= x
        // with all target bits is x rounded up to the target's
        // low j bits, costing (target & mask) - (x & mask) with
        // mask = 2^j - 1 (and 0 when x already covers the
        // target). The m cheapest such costs decide whether the
        // bit survives.
        int mx = 0;
        for (int x : nums) mx = Math.max(mx, x);
        mx = 32 - Integer.numberOfLeadingZeros(mx + k);
        int n = nums.length;
        int ans = 0;
        int[] cost = new int[n];
        for (int bit = mx - 1; bit >= 0; bit--) {
            int target = ans | (1 << bit);
            for (int i = 0; i < n; i++) {
                int x = nums[i];
                int diff = target & ~x;
                int j = diff == 0 ? 0 : 32 - Integer.numberOfLeadingZeros(diff);
                long mask = (1L << j) - 1;
                cost[i] = (int) ((target & mask) - (x & mask));
            }
            Arrays.sort(cost);
            long sum = 0;
            for (int i = 0; i < m; i++) sum += cost[i];
            if (sum <= k) ans = target;
        }
        return ans;
    }
}
