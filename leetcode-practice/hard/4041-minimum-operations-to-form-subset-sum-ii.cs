// LeetCode 4041. Minimum Operations to Form Subset Sum II — Hard
// https://leetcode.com/problems/minimum-operations-to-form-subset-sum-ii/
// Submission 2203529384 — Accepted, C#
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums, int sum) {
        // My thinking: each element can be divided and
        // doubled in any order, and any sequence of d
        // divisions and m doublings lands on (x >> d) << m
        // — dividing drops low bits, doubling appends
        // zeroes — so for every d the reachable values are
        // base, 2*base, 4*base, ... with costs d, d+1,
        // d+2, ... . Keep the cheapest cost for each value
        // up to sum: values above sum can never join a
        // subset summing to sum, and doubling past sum and
        // dividing back only wastes operations, since
        // floor(2u / 2) is exactly u again. Then it is a
        // 0/1 knapsack over the target sum: dp[s] is the
        // fewest operations to reach sum s with the elements
        // handled so far, and each element either stays out
        // or joins with one of its reachable values. The
        // update reads only the previous layer, so no
        // element is ever used twice.
        const int INF = 1000000000;
        int[] dp = new int[sum + 1];
        Array.Fill(dp, INF);
        dp[0] = 0;
        foreach (int x in nums) {
            var opts = new Dictionary<int, int>();
            int d = 0;
            while (true) {
                int b = x >> d;
                int v = b, c = d;
                while (v <= sum) {
                    if (!opts.TryGetValue(v, out int old) || c < old) {
                        opts[v] = c;
                    }
                    if (v == 0) {
                        break;
                    }
                    v *= 2;
                    c++;
                }
                if (b == 0) {
                    break;
                }
                d++;
            }
            int[] ndp = (int[])dp.Clone();
            foreach (var kv in opts) {
                int v = kv.Key, c = kv.Value;
                if (v == 0) {
                    continue;
                }
                for (int s = 0; s + v <= sum; s++) {
                    if (dp[s] != INF && dp[s] + c < ndp[s + v]) {
                        ndp[s + v] = dp[s] + c;
                    }
                }
            }
            dp = ndp;
        }
        return dp[sum] == INF ? -1 : dp[sum];
    }
}
