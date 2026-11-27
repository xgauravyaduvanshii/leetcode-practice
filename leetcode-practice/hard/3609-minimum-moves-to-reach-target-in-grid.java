// LeetCode 3609. Minimum Moves to Reach Target in Grid — Hard
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/
// Submission 2202872638 — Accepted, Java
class Solution {
    private int sx, sy;

    public int minMoves(int sx, int sy, int tx, int ty) {
        // My thinking: I walk backwards from the target. When the
        // coordinates differ, the larger one tells me the last move:
        // if it is at least twice the smaller, the step must have
        // doubled it, so I halve it (and an odd value means the
        // target is unreachable); otherwise I subtract the smaller
        // one. When the coordinates are equal, the last move came
        // from (0, y) or (x, 0), so I try both predecessors — that
        // is the case the first attempt missed.
        this.sx = sx;
        this.sy = sy;
        return rev(tx, ty, 0);
    }

    private int rev(long x, long y, int moves) {
        while (true) {
            if (x == sx && y == sy) return moves;
            if (x < sx || y < sy) return -1;
            if (x == y) {
                int r1 = rev(0, y, moves + 1);
                if (r1 != -1) return r1;
                return rev(x, 0, moves + 1);
            } else if (x > y) {
                if (x >= 2 * y) {
                    if (x % 2 == 1) return -1;
                    x /= 2;
                } else {
                    x -= y;
                }
                moves++;
            } else {
                if (y >= 2 * x) {
                    if (y % 2 == 1) return -1;
                    y /= 2;
                } else {
                    y -= x;
                }
                moves++;
            }
        }
    }
}
