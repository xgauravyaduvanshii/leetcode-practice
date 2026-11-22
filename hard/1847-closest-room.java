// LeetCode 1847. Closest Room — Hard
// https://leetcode.com/problems/closest-room/
// Submission 2201198447 — Accepted, Java
//
// My thinking: I sort the rooms and the queries
// by size, then sweep the queries from biggest to
// smallest, keeping the room ids that qualify in
// a sorted set and taking the id nearest to the
// preferred one.

import java.util.*;

class Solution {
    public int[] closestRoom(int[][] rooms, int[][] queries) {
        Arrays.sort(rooms, (a, b) -> b[1] - a[1]);
        Integer[] order = new Integer[queries.length];
        for (int i = 0; i < queries.length; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> queries[b][1] - queries[a][1]);
        TreeSet<Integer> ids = new TreeSet<>();
        int[] ans = new int[queries.length];
        int j = 0;
        for (int qi : order) {
            int pref = queries[qi][0];
            int minSize = queries[qi][1];
            while (j < rooms.length && rooms[j][1] >= minSize) {
                ids.add(rooms[j][0]);
                j++;
            }
            if (ids.isEmpty()) {
                ans[qi] = -1;
                continue;
            }
            Integer hi = ids.ceiling(pref);
            Integer lo = ids.floor(pref);
            int best = -1;
            if (hi != null) best = hi;
            if (lo != null && (best == -1 || pref - lo <= best - pref)) best = lo;
            ans[qi] = best;
        }
        return ans;
    }
}
