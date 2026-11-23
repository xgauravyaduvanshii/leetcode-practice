// LeetCode 3235. Check if the Rectangle Corner Is Reachable — Hard
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/
// Submission 2202117350 — Accepted, C#
//
// My thinking: the corner is unreachable
// exactly when the circles chain together
// into a barrier across the rectangle —
// left to right, left to bottom, right to
// top, or top to bottom. I union circles
// with the four edges, but two circles
// only union when their lens actually
// meets the rectangle, which I check with
// their intersection points, centres,
// corners and edge crossings.

public class Solution {
    public bool CanReachCorner(int xCorner, int yCorner, int[][] circles) {
        long X = xCorner, Y = yCorner;
        int n = circles.Length;
        int[] parent = new int[n + 4];
        for (int i = 0; i < parent.Length; i++) parent[i] = i;
        int Find(int x) {
            while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
            return x;
        }
        void Union(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra != rb) parent[ra] = rb;
        }
        long Clamp(long v, long lo, long hi) { return v < lo ? lo : (v > hi ? hi : v); }
        bool CircleEdgeHit(long cx, long cy, long rr, long ox, long oy, long orr) {
            if (Math.Abs(cx) <= rr) {
                double dd = Math.Sqrt((double)rr * rr - (double)cx * cx);
                foreach (double py in new double[] { cy - dd, cy + dd }) {
                    if (py >= 0 && py <= Y && Math.Sqrt((double)ox * ox + (py - oy) * (py - oy)) <= orr + 1e-7) return true;
                }
            }
            if (Math.Abs(cx - X) <= rr) {
                double dd = Math.Sqrt((double)rr * rr - (double)(cx - X) * (cx - X));
                foreach (double py in new double[] { cy - dd, cy + dd }) {
                    if (py >= 0 && py <= Y && Math.Sqrt((double)(X - ox) * (X - ox) + (py - oy) * (py - oy)) <= orr + 1e-7) return true;
                }
            }
            if (Math.Abs(cy) <= rr) {
                double dd = Math.Sqrt((double)rr * rr - (double)cy * cy);
                foreach (double px in new double[] { cx - dd, cx + dd }) {
                    if (px >= 0 && px <= X && Math.Sqrt((px - ox) * (px - ox) + (double)oy * oy) <= orr + 1e-7) return true;
                }
            }
            if (Math.Abs(cy - Y) <= rr) {
                double dd = Math.Sqrt((double)rr * rr - (double)(cy - Y) * (cy - Y));
                foreach (double px in new double[] { cx - dd, cx + dd }) {
                    if (px >= 0 && px <= X && Math.Sqrt((px - ox) * (px - ox) + (double)(Y - oy) * (Y - oy)) <= orr + 1e-7) return true;
                }
            }
            return false;
        }
        bool LensInRect(long x1, long y1, long r1, long x2, long y2, long r2) {
            long dx = x2 - x1, dy = y2 - y1;
            long d2 = dx * dx + dy * dy;
            if (d2 == 0) {
                long cx, cy, rr;
                if (r1 <= r2) { cx = x1; cy = y1; rr = r1; } else { cx = x2; cy = y2; rr = r2; }
                long clx = Clamp(cx, 0, X), cly = Clamp(cy, 0, Y);
                return (cx - clx) * (cx - clx) + (cy - cly) * (cy - cly) <= rr * rr;
            }
            if (x1 >= 0 && x1 <= X && y1 >= 0 && y1 <= Y && (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= r2 * r2) return true;
            if (x2 >= 0 && x2 <= X && y2 >= 0 && y2 <= Y && (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= r1 * r1) return true;
            foreach (var c in new long[][] { new long[] { 0, 0 }, new long[] { X, 0 }, new long[] { 0, Y }, new long[] { X, Y } }) {
                if ((c[0] - x1) * (c[0] - x1) + (c[1] - y1) * (c[1] - y1) <= r1 * r1 && (c[0] - x2) * (c[0] - x2) + (c[1] - y2) * (c[1] - y2) <= r2 * r2) return true;
            }
            double d = Math.Sqrt((double)d2);
            double a = ((double)r1 * r1 - (double)r2 * r2 + (double)d2) / (2.0 * d);
            double h2 = (double)r1 * r1 - a * a;
            if (h2 >= 0) {
                double h = Math.Sqrt(h2);
                double xm = x1 + a * dx / d, ym = y1 + a * dy / d;
                double rx = -dy * h / d, ry = dx * h / d;
                foreach (var p in new double[][] { new double[] { xm + rx, ym + ry }, new double[] { xm - rx, ym - ry } }) {
                    if (p[0] >= -1e-7 && p[0] <= X + 1e-7 && p[1] >= -1e-7 && p[1] <= Y + 1e-7) return true;
                }
            }
            if (CircleEdgeHit(x1, y1, r1, x2, y2, r2)) return true;
            if (CircleEdgeHit(x2, y2, r2, x1, y1, r1)) return true;
            return false;
        }
        int TOP = n, RIGHT = n + 1, BOTTOM = n + 2, LEFT = n + 3;
        for (int i = 0; i < n; i++) {
            long x = circles[i][0], y = circles[i][1], r = circles[i][2];
            long r2 = r * r;
            long cy = Clamp(y, 0, Y);
            if (x * x + (y - cy) * (y - cy) <= r2) Union(i, LEFT);
            if ((x - X) * (x - X) + (y - cy) * (y - cy) <= r2) Union(i, RIGHT);
            long cx = Clamp(x, 0, X);
            if ((x - cx) * (x - cx) + y * y <= r2) Union(i, BOTTOM);
            if ((x - cx) * (x - cx) + (y - Y) * (y - Y) <= r2) Union(i, TOP);
            for (int j = 0; j < i; j++) {
                long x2 = circles[j][0], y2 = circles[j][1], r2c = circles[j][2];
                if ((x - x2) * (x - x2) + (y - y2) * (y - y2) <= (r + r2c) * (r + r2c)) {
                    if (LensInRect(x, y, r, x2, y2, r2c)) Union(i, j);
                }
            }
        }
        if (Find(LEFT) == Find(RIGHT)) return false;
        if (Find(LEFT) == Find(BOTTOM)) return false;
        if (Find(RIGHT) == Find(TOP)) return false;
        if (Find(TOP) == Find(BOTTOM)) return false;
        return true;
    }
}
