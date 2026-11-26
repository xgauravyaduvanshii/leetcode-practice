// LeetCode 4013. Count Subarrays With Even Odd Ratio II — Hard
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/
// Submission 2203510648 — Accepted, Java
import java.util.Arrays;

class Solution {
    public long countRatioSubarrays(int[] nums, int a, int b) {
        // My thinking: a subarray with x evens and y odds
        // is valid exactly when y > 0 and b*x <= a*y.
        // Give each element a score: +b for an even element,
        // -a for an odd one. Then a subarray's score is
        // b*x - a*y, so it is valid exactly when its score
        // is at most 0. An all-even subarray can never
        // qualify anyway (its score is positive), so the
        // y > 0 condition needs no separate check. With
        // prefix sums P, a subarray is valid exactly when
        // P[l] >= P[r] for l < r. Counting such pairs is a
        // classic inversion count: sweep the prefix sums
        // from left to right, keeping them in a Fenwick
        // tree over compressed coordinates, and for each
        // new prefix add how many earlier ones are at
        // least as large.
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + (nums[i] % 2 == 0 ? b : -a);
        }
        long[] vals = pref.clone();
        Arrays.sort(vals);
        int m = 0;
        for (int i = 0; i < vals.length; i++) {
            if (i == 0 || vals[i] != vals[i - 1]) {
                vals[m++] = vals[i];
            }
        }
        long[] bit = new long[m + 2];
        long ans = 0;
        long seen = 0;
        for (long p : pref) {
            int idx = Arrays.binarySearch(vals, 0, m, p) + 1;
            long less = 0;
            for (int i = idx - 1; i > 0; i -= i & -i) {
                less += bit[i];
            }
            ans += seen - less;
            for (int i = idx; i < bit.length; i += i & -i) {
                bit[i]++;
            }
            seen++;
        }
        return ans;
    }
}
