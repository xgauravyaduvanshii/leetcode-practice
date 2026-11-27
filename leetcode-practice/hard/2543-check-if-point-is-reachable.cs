// LeetCode 2543. Check if Point Is Reachable — Hard
// https://leetcode.com/problems/check-if-point-is-reachable/
// Submission 2201806600 — Accepted, C#
//
// My thinking: I shrink the target
// back toward (1, 1) — halving whenever
// a coordinate is even, and when both
// are odd I take the smaller away from
// the larger, the way Euclid would — if
// I land on (1, 1) the point is
// reachable.

public class Solution {
    public bool IsReachable(int targetX, int targetY) {
        long x = targetX, y = targetY;
        while (x > 1 || y > 1) {
            if (x % 2 == 0) x /= 2;
            else if (y % 2 == 0) y /= 2;
            else if (x > y) x -= y;
            else if (y > x) y -= x;
            else return false;
        }
        return x == 1 && y == 1;
    }
}
