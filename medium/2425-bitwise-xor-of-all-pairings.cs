// LeetCode 2425. Bitwise XOR of All Pairings — Medium
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/
// Submission 2204862574 — Accepted, C#
//
// My thinking: same idea as the Python version — each value is XORed
// as many times as the other array is long, so only the XORs whose
// count is odd survive.
public class Solution {
    public int XorAllNums(int[] nums1, int[] nums2) {
        int ans = 0;
        if (nums2.Length % 2 == 1) {
            foreach (int x in nums1) ans ^= x;
        }
        if (nums1.Length % 2 == 1) {
            foreach (int x in nums2) ans ^= x;
        }
        return ans;
    }
}
