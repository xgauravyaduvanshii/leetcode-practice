// LeetCode 3161. Block Placement Queries — Hard
// https://leetcode.com/problems/block-placement-queries/
// Submission 2202051819 — Accepted, Java
//
// My thinking: a query asks whether some
// gap between consecutive obstacles,
// starting at or before x - sz, is at
// least sz wide. I keep the gaps in a
// segment tree over positions and the
// obstacles in a sorted set, so inserting
// an obstacle updates just the two gaps
// it splits and each query is answered
// from the biggest gap seen so far.

import java.util.*;

class Solution {
    public List<Boolean> getResults(int[][] queries) {
        int maxX = 0;
        for (int[] q : queries) maxX = Math.max(maxX, q[1]);
        int size = 1;
        while (size <= maxX) size <<= 1;
        int[] seg = new int[2 * size];
        seg[size] = 1000000000;
        for (int i = size - 1; i >= 1; i--) seg[i] = Math.max(seg[2 * i], seg[2 * i + 1]);
        TreeSet<Integer> obs = new TreeSet<>();
        List<Boolean> res = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) {
                int x = q[1];
                Integer pred = obs.lower(x);
                Integer succ = obs.higher(x);
                int left = pred == null ? 0 : pred;
                update(seg, size, left, x - left);
                update(seg, size, x, succ == null ? 1000000000 : succ - x);
                obs.add(x);
            } else {
                int x = q[1], sz = q[2];
                int X = x - sz;
                if (X < 0) res.add(false);
                else res.add(query(seg, size, X) >= sz);
            }
        }
        return res;
    }
    private void update(int[] seg, int size, int pos, int val) {
        int p = pos + size;
        seg[p] = val;
        for (p >>= 1; p >= 1; p >>= 1) {
            seg[p] = Math.max(seg[2 * p], seg[2 * p + 1]);
            if (p == 1) break;
        }
    }
    private int query(int[] seg, int size, int r) {
        int l = size, rr = r + size, ans = 0;
        while (l <= rr) {
            if ((l & 1) == 1) ans = Math.max(ans, seg[l++]);
            if ((rr & 1) == 0) ans = Math.max(ans, seg[rr--]);
            l >>= 1;
            rr >>= 1;
        }
        return ans;
    }
}
