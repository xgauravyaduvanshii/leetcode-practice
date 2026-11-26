// LeetCode 4123. Minimum Cost to Delete Array — Hard
// https://leetcode.com/problems/minimum-cost-to-delete-array/
// Submission 2203746927 — Accepted, Java
class Solution {
    public long minCost(int[] nums) {
        // My thinking: every operation pays the first and
        // last elements of the chosen subarray, so the
        // first and last elements of the whole array are
        // each paid exactly once, no matter what. An
        // interior element is paid only when it becomes
        // an endpoint of some operation, and the interior
        // elements that get paid form an even-sized
        // subset (endpoints come in pairs). So the answer
        // is nums[0] + nums[n-1] plus the minimum sum of
        // an even-sized subset of the interior. Track two
        // states while scanning the interior: even = best
        // sum with an even count chosen so far, odd = best
        // sum with an odd count. For each x we may skip it
        // or take it (flipping parity); the empty subset
        // keeps even at 0, so we never take a positive-sum
        // subset. The answer adds the even state.
        long INF = Long.MAX_VALUE / 4;
        long even = 0;
        long odd = INF;
        for (int i = 1; i < nums.length - 1; i++) {
            long x = nums[i];
            long newEven = Math.min(even, odd + x);
            long newOdd = Math.min(odd, even + x);
            even = newEven;
            odd = newOdd;
        }
        return (long) nums[0] + nums[nums.length - 1] + even;
    }
}
