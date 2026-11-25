// LeetCode 3695. Maximize Alternating Sum Using Swaps — Hard
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/
// Submission 2203046180 — Accepted, C#
using System;
using System.Collections.Generic;

public class Solution {
    public long MaxAlternatingSum(int[] nums, int[][] swaps) {
        // My thinking: swaps link indices into connected components,
        // and inside one component the values can be rearranged
        // freely, since any permutation is reachable by swaps. An
        // even index adds its value to the sum and an odd index
        // subtracts it, so in each component I put the biggest
        // values on the even spots and the smallest on the odd ones.
        int n = nums.Length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        foreach (int[] swap in swaps) {
            int rp = Find(swap[0]);
            int rq = Find(swap[1]);
            if (rp != rq) parent[rp] = rq;
        }

        var groups = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            int root = Find(i);
            if (!groups.ContainsKey(root)) groups[root] = new List<int>();
            groups[root].Add(i);
        }

        long ans = 0;
        foreach (List<int> idxs in groups.Values) {
            var vals = new List<int>();
            int evens = 0;
            foreach (int i in idxs) {
                vals.Add(nums[i]);
                if (i % 2 == 0) evens++;
            }
            vals.Sort((a, b) => b.CompareTo(a));
            for (int i = 0; i < vals.Count; i++) {
                ans += i < evens ? vals[i] : -vals[i];
            }
        }
        return ans;
    }
}
