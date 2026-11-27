// LeetCode 2709. Greatest Common Divisor Traversal — Hard
// https://leetcode.com/problems/greatest-common-divisor-traversal/
// Submission 2201872405 — Accepted, C#
//
// My thinking: two numbers can meet
// only through a prime they share, so
// I tie every number to its primes and
// let the primes tie the numbers to
// each other — if every number ends up
// in one family, the whole array is
// connected. A 1 has no prime, so it
// stands alone.

using System;
using System.Collections.Generic;

public class Solution {
    private int[] parent;
    private int Find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    private void Union(int a, int b) {
        int ra = Find(a), rb = Find(b);
        if (ra != rb) parent[ra] = rb;
    }

    public bool CanTraverseAllPairs(int[] nums) {
        int n = nums.Length;
        if (n == 1) return true;
        foreach (int x in nums) if (x == 1) return false;
        int mx = 0;
        foreach (int x in nums) mx = Math.Max(mx, x);
        int[] spf = new int[mx + 1];
        for (int i = 0; i <= mx; i++) spf[i] = i;
        for (int i = 2; i * i <= mx; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= mx; j += i) {
                    if (spf[j] == j) spf[j] = i;
                }
            }
        }
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        var first = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            var primes = new HashSet<int>();
            while (x > 1) {
                int p = spf[x];
                primes.Add(p);
                while (x % p == 0) x /= p;
            }
            foreach (int p in primes) {
                if (first.ContainsKey(p)) Union(i, first[p]);
                else first[p] = i;
            }
        }
        int root = Find(0);
        for (int i = 1; i < n; i++) if (Find(i) != root) return false;
        return true;
    }
}
