// LeetCode 2584. Split the Array to Make Coprime Products — Hard
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/
// Submission 2201837437 — Accepted, Java
//
// My thinking: a split fails exactly
// when some prime lives on both sides of
// it, so I learn where every prime
// starts and ends, then walk the split
// forward keeping the furthest any prime
// seen so far still reaches — the first
// split it never reaches past is the
// answer.

import java.util.*;

class Solution {
    public int findValidSplit(int[] nums) {
        int n = nums.length;
        int mx = 0;
        for (int x : nums) mx = Math.max(mx, x);
        if (mx < 2) return n >= 2 ? 0 : -1;
        int[] spf = new int[mx + 1];
        for (int i = 0; i <= mx; i++) spf[i] = i;
        for (int i = 2; i * i <= mx; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= mx; j += i) {
                    if (spf[j] == j) spf[j] = i;
                }
            }
        }
        Map<Integer, Integer> last = new HashMap<>();
        for (int idx = 0; idx < n; idx++) {
            int v = nums[idx];
            while (v > 1) {
                int p = spf[v];
                last.put(p, idx);
                while (v % p == 0) v /= p;
            }
        }
        int maxLast = -1;
        for (int i = 0; i < n - 1; i++) {
            int v = nums[i];
            while (v > 1) {
                int p = spf[v];
                maxLast = Math.max(maxLast, last.get(p));
                while (v % p == 0) v /= p;
            }
            if (maxLast <= i) return i;
        }
        return -1;
    }
}
