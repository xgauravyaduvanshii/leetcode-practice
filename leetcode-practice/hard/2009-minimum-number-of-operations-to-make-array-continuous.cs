// LeetCode 2009. Minimum Number of Operations to Make Array Continuous — Hard
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
// Submission 2201312585 — Accepted, C#
//
// My thinking: I only keep the distinct values
// that already fit inside one window of length n,
// and the biggest such window tells me how few
// changes I need.

using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        var uniq = new SortedSet<int>(nums);
        var arr = new List<int>(uniq);
        int best = 0, right = 0;
        for (int left = 0; left < arr.Count; left++) {
            while (right < arr.Count && arr[right] - arr[left] < n) {
                right++;
            }
            best = Math.Max(best, right - left);
        }
        return n - best;
    }
}
