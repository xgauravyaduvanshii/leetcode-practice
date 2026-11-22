// LeetCode 1835. Find XOR Sum of All Pairs Bitwise AND — Hard
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/
// Submission 2201193663 — Accepted, C#
//
// My thinking: a bit survives the xor of all
// pairs exactly when it is set in an odd number
// of entries on both sides — which is just the
// xor of each array, anded together.

public class Solution {
    public int GetXORSum(int[] arr1, int[] arr2) {
        int x1 = 0;
        foreach (int v in arr1) x1 ^= v;
        int x2 = 0;
        foreach (int v in arr2) x2 ^= v;
        return x1 & x2;
    }
}
