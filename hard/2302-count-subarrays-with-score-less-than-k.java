// LeetCode 2302. Count Subarrays With Score Less Than K — Hard
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
// Submission 2201667750 — Accepted, Java
//
// My thinking: every number is positive,
// so a window's score only grows as it
// widens — I slide the right edge out and
// pull the left edge in until the score
// fits, and every start the window still
// covers is one more good subarray.

class Solution {
    public long countSubarrays(int[] nums, long k) {
        long total = 0;
        long window = 0;
        int left = 0;
        for (int right = 0; right < nums.length; right++) {
            window += nums[right];
            while (window * (right - left + 1) >= k) {
                window -= nums[left];
                left++;
            }
            total += right - left + 1;
        }
        return total;
    }
}
