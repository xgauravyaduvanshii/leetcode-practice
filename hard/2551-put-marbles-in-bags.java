// LeetCode 2551. Put Marbles in Bags — Hard
// https://leetcode.com/problems/put-marbles-in-bags/
// Submission 2201811405 — Accepted, Java
//
// My thinking: every split between two
// bags adds the pair of marbles it
// touches, so the whole score is the
// first and last marble plus the pairs
// at the cuts — the dearest cuts and the
// cheapest cuts give the two extremes,
// and their gap is the answer.

import java.util.Arrays;

class Solution {
    public long putMarbles(int[] weights, int k) {
        int n = weights.length;
        if (k == 1 || n == k) return 0;
        long[] pairs = new long[n - 1];
        for (int i = 0; i < n - 1; i++) {
            pairs[i] = (long) weights[i] + weights[i + 1];
        }
        Arrays.sort(pairs);
        long maxSum = 0, minSum = 0;
        for (int i = 0; i < k - 1; i++) {
            minSum += pairs[i];
            maxSum += pairs[n - 2 - i];
        }
        return maxSum - minSum;
    }
}
