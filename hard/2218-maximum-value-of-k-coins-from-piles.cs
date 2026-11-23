// LeetCode 2218. Maximum Value of K Coins From Piles — Hard
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
// Submission 2201626987 — Accepted, C#
//
// My thinking: coins come off the top of
// each pile in order, so I price every pile
// by how many I take from it, then share
// exactly k coins across the piles for the
// best total.

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxValueOfCoins(IList<IList<int>> piles, int k) {
        var prefs = new List<int[]>();
        foreach (var pile in piles) {
            var pref = new int[pile.Count + 1];
            for (int i = 0; i < pile.Count; i++) {
                pref[i + 1] = pref[i] + pile[i];
            }
            prefs.Add(pref);
        }
        var dp = new int[k + 1];
        foreach (var pref in prefs) {
            var newDp = new int[k + 1];
            for (int j = 0; j <= k; j++) {
                int best = dp[j];
                for (int t = 1; t <= Math.Min(pref.Length - 1, j); t++) {
                    best = Math.Max(best, dp[j - t] + pref[t]);
                }
                newDp[j] = best;
            }
            dp = newDp;
        }
        return dp[k];
    }
}
