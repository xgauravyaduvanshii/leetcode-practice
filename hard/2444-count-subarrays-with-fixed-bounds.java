// LeetCode 2444. Count Subarrays With Fixed Bounds — Hard
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
// Submission 2201746399 — Accepted, Java
//
// My thinking: a fixed-bound subarray must
// contain both minK and maxK and nothing
// outside their range — I sweep the right
// end along, remembering where each bound
// was last seen and where the last
// out-of-range value fell, and every
// left end up to the nearer bound works.

class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        long ans = 0;
        int lastMin = -1, lastMax = -1, lastBad = -1;
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (x < minK || x > maxK) lastBad = i;
            if (x == minK) lastMin = i;
            if (x == maxK) lastMax = i;
            ans += Math.max(0, Math.min(lastMin, lastMax) - lastBad);
        }
        return ans;
    }
}
