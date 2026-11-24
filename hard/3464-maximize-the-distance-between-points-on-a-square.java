// LeetCode 3464. Maximize the Distance Between Points on a Square — Hard
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/
// Submission 2202653238 — Accepted 621/621, Java
//
// My thinking: I sort the points by where they sit on the square's
// perimeter and binary-search the answer. For a candidate distance d I try
// every point as the first pick and greedily take the next point that is
// at least d away (Manhattan) from every point picked so far, staying
// inside one trip around the perimeter. Trying every start matters: a
// single start fails, because the best set need not contain the leftmost
// point, and the Manhattan distance is not the perimeter distance (two
// points on opposite sides can be close across the middle while far apart
// along the edge), so the greedy must check a new point against all
// picked points, not just the last one. The perimeter positions reach
// 4 * side, up to 4e9, which overflows int, so positions and the binary
// search use long; the answer itself fits in int.

import java.util.Arrays;

class Solution {
    public int maxDistance(int side, int[][] points, int k) {
        int n = points.length;
        long per = 4L * side;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Long.compare(pos(points[a], side), pos(points[b], side)));
        long[] t = new long[2 * n];
        int[][] pts = new int[2 * n][];
        for (int i = 0; i < n; i++) {
            t[i] = pos(points[idx[i]], side);
            pts[i] = points[idx[i]];
            t[i + n] = t[i] + per;
            pts[i + n] = pts[i];
        }
        long lo = 0, hi = 2L * side;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (ok(mid, t, pts, n, per, k)) lo = mid;
            else hi = mid - 1;
        }
        return (int) lo;
    }

    private long pos(int[] p, int side) {
        int x = p[0], y = p[1];
        if (y == 0) return x;
        if (x == side) return (long) side + y;
        if (y == side) return 2L * side + (side - x);
        return 3L * side + (side - y);
    }

    private boolean ok(long d, long[] t, int[][] pts, int n, long per, int k) {
        if (d <= 0) return true;
        int[] sel = new int[k];
        for (int s = 0; s < n; s++) {
            sel[0] = s;
            int picked = 1;
            int cur = s;
            while (picked < k) {
                int nxt = -1;
                for (int j = cur + 1; j < s + n; j++) {
                    if (t[j] - t[s] >= per) break;
                    boolean good = true;
                    for (int q = 0; q < picked; q++) {
                        int pp = sel[q];
                        long dist = Math.abs((long) pts[j][0] - pts[pp][0])
                                + Math.abs((long) pts[j][1] - pts[pp][1]);
                        if (dist < d) {
                            good = false;
                            break;
                        }
                    }
                    if (good) {
                        nxt = j;
                        break;
                    }
                }
                if (nxt == -1) break;
                sel[picked++] = nxt;
                cur = nxt;
            }
            if (picked == k) return true;
        }
        return false;
    }
}
