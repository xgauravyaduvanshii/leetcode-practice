// LeetCode 1879. Minimum XOR Sum of Two Arrays — Hard
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
// Submission 2201214565 — Accepted, C#
//
// My thinking: I assign the second array to the
// first one element at a time and keep, for every
// set of already-used positions, the cheapest xor
// sum so far — a bitmask holds which positions
// are taken.

using System;

public class Solution {
    public int MinimumXORSum(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int[] dp = new int[1 << n];
        for (int i = 0; i < dp.Length; i++) dp[i] = int.MaxValue;
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int i = 0;
            for (int b = 0; b < n; b++) if ((mask >> b & 1) == 1) i++;
            if (i >= n) continue;
            for (int j = 0; j < n; j++) {
                if ((mask >> j & 1) == 0) {
                    dp[mask | (1 << j)] = Math.Min(dp[mask | (1 << j)], dp[mask] + (nums1[i] ^ nums2[j]));
                }
            }
        }
        return dp[(1 << n) - 1];
    }
}
