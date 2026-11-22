// LeetCode 1793. Maximum Score of a Good Subarray — Hard
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/
// Submission 2201168699 — Accepted, C#
//
// My thinking: the subarray must contain k, so I
// grow out from k one step at a time, always
// reaching for the taller side first — that keeps
// the minimum as high as possible for as long as
// possible.

using System;

public class Solution {
    public int MaximumScore(int[] nums, int k) {
        int n = nums.Length;
        int left = k, right = k;
        int curMin = nums[k];
        int best = nums[k];
        while (left > 0 || right < n - 1) {
            if (right == n - 1 || (left > 0 && nums[left - 1] > nums[right + 1])) {
                left--;
                curMin = Math.Min(curMin, nums[left]);
            } else {
                right++;
                curMin = Math.Min(curMin, nums[right]);
            }
            best = Math.Max(best, curMin * (right - left + 1));
        }
        return best;
    }
}
