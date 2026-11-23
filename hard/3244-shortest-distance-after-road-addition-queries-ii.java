// LeetCode 3244. Shortest Distance After Road Addition Queries II — Hard
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
// Submission 2202129364 — Accepted, Java
//
// My thinking: the chain edges alone give a
// distance of n - 1. Each query (u, v) can
// only help by skipping the chain nodes strictly
// between u and v. I keep the still-alive nodes
// in a TreeSet, so each skipped node is removed
// once and the distance drops by 1 per removal.

import java.util.TreeSet;

class Solution {
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            set.add(i);
        }
        int dist = n - 1;
        int[] ans = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int u = queries[q][0];
            int v = queries[q][1];
            Integer x = set.higher(u);
            while (x != null && x < v) {
                Integer nxt = set.higher(x);
                set.remove(x);
                dist--;
                x = nxt;
            }
            ans[q] = dist;
        }
        return ans;
    }
}
