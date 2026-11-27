// LeetCode 3288. Length of the Longest Increasing Path — Hard
// https://leetcode.com/problems/length-of-the-longest-increasing-path/
// Submission 2202182973 — Accepted, Java
//
// My thinking: any increasing path through
// coordinates[k] is an increasing chain before
// it plus one plus an increasing chain after
// it. The two sides are independent, and each
// side's longest chain is a plain LIS on the
// y-values after sorting by x (ties broken by
// y descending so equal x never chains).

import java.util.*;

class Solution {
    public int maxPathLength(int[][] coordinates, int k) {
        int xk = coordinates[k][0];
        int yk = coordinates[k][1];
        List<int[]> before = new ArrayList<>();
        List<int[]> after = new ArrayList<>();
        for (int[] p : coordinates) {
            if (p[0] < xk && p[1] < yk) before.add(p);
            else if (p[0] > xk && p[1] > yk) after.add(p);
        }
        return lis(before) + 1 + lis(after);
    }

    private int lis(List<int[]> pts) {
        pts.sort((a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(b[1], a[1]));
        List<Integer> tails = new ArrayList<>();
        for (int[] p : pts) {
            int y = p[1];
            int idx = Collections.binarySearch(tails, y);
            if (idx < 0) idx = -idx - 1;
            if (idx == tails.size()) tails.add(y);
            else tails.set(idx, y);
        }
        return tails.size();
    }
}
