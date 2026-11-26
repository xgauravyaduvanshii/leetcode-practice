// LeetCode 2002. Maximum Product of the Length of Two Palindromic Subsequences — Medium
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
// Submission 2204125398 — Accepted, C#

// My thinking: the string is at most 12 characters long, so there are
// only 2^12 = 4096 possible subsequences, and I can look at every one
// of them by its bitmask: bit i set means character s[i] is part of the
// subsequence. For each mask I build its subsequence and check whether
// it reads the same forwards and backwards; if it does, I record the
// mask's length. Two subsequences are allowed together only when they
// use no character in common, which for bitmasks is simply
// mask1 & mask2 == 0. So I try every pair of palindromic masks that do
// not overlap and keep the biggest product of their lengths. With at
// most 4096 masks this pair check is cheap, and it is guaranteed to
// find the best answer because every possible pair of disjoint
// palindromic subsequences is examined exactly once.
using System.Collections.Generic;

public class Solution {
    public int MaxProduct(string s) {
        int n = s.Length;
        var palLen = new Dictionary<int, int>();
        for (int mask = 1; mask < (1 << n); mask++) {
            var chars = new List<char>();
            for (int i = 0; i < n; i++) {
                if ((mask >> i & 1) == 1) chars.Add(s[i]);
            }
            bool isPal = true;
            for (int l = 0, r = chars.Count - 1; l < r; l++, r--) {
                if (chars[l] != chars[r]) { isPal = false; break; }
            }
            if (isPal) palLen[mask] = chars.Count;
        }

        int best = 0;
        var masks = new List<int>(palLen.Keys);
        for (int i = 0; i < masks.Count; i++) {
            for (int j = i; j < masks.Count; j++) {
                int m1 = masks[i], m2 = masks[j];
                if ((m1 & m2) == 0) {
                    best = System.Math.Max(best, palLen[m1] * palLen[m2]);
                }
            }
        }
        return best;
    }
}
