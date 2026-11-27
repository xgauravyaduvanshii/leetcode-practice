// LeetCode 2411. Smallest Subarrays With Maximum Bitwise OR — Medium
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
// Submission 2204793041 — Accepted, Java
//
// My thinking: same idea as the Python version — the max OR from i is
// the suffix OR; for each bit set in it, the answer must reach that
// bit's last occurrence at or after i, and the farthest such position
// gives the shortest subarray.
class Solution {
    public int[] smallestSubarrays(int[] nums) {
        int n = nums.length;
        int[] suf = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suf[i] = suf[i + 1] | nums[i];
        }
        int[] nxt = new int[31];
        java.util.Arrays.fill(nxt, n);
        int[] ans = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            for (int b = 0; b < 31; b++) {
                if (((nums[i] >> b) & 1) == 1) {
                    nxt[b] = i;
                }
            }
            int j = i;
            int x = suf[i];
            for (int b = 0; b < 31; b++) {
                if (((x >> b) & 1) == 1) {
                    j = Math.max(j, nxt[b]);
                }
            }
            ans[i] = j - i + 1;
        }
        return ans;
    }
}
