# LeetCode 2543. Check if Point Is Reachable — Hard
# https://leetcode.com/problems/check-if-point-is-reachable/
# Submission 2201805933 — Accepted, Python3
#
# My thinking: I shrink the target
# back toward (1, 1) — halving whenever
# a coordinate is even, and when both
# are odd I take the smaller away from
# the larger, the way Euclid would — if
# I land on (1, 1) the point is
# reachable.

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        x, y = targetX, targetY
        while x > 1 or y > 1:
            if x % 2 == 0:
                x //= 2
            elif y % 2 == 0:
                y //= 2
            elif x > y:
                x -= y
            elif y > x:
                y -= x
            else:
                return False
        return x == 1 and y == 1
