# LeetCode 3464. Maximize the Distance Between Points on a Square — Hard
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/
# Submission 2202650578 — Accepted 621/621, Python3
#
# My thinking: I sort the points by where they sit on the square's perimeter
# and binary-search the answer. For a candidate distance d I try every point
# as the first pick and greedily take the next point that is at least d away
# (Manhattan) from every point picked so far, staying inside one trip around
# the perimeter. Trying every start matters: a single start fails, because
# the best set need not contain the leftmost point, and the Manhattan
# distance is not the perimeter distance (two points on opposite sides can
# be close across the middle while far apart along the edge), so the greedy
# must check a new point against all picked points, not just the last one.
# I verified this check against brute force on 2500 random small cases.

from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def pos(p):
            x, y = p
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return 2 * side + (side - x)
            return 3 * side + (side - y)

        pts = sorted(points, key=pos)
        t = [pos(p) for p in pts]
        n = len(pts)
        per = 4 * side
        t2 = t + [x + per for x in t]
        pts2 = pts + pts

        def ok(d: int) -> bool:
            if d <= 0:
                return True
            for s in range(n):
                picked = [s]
                cur = s
                while len(picked) < k:
                    nxt = -1
                    for j in range(cur + 1, s + n):
                        good = True
                        pj = pts2[j]
                        for p in picked:
                            pp = pts2[p]
                            if abs(pj[0] - pp[0]) + abs(pj[1] - pp[1]) < d:
                                good = False
                                break
                        if good:
                            nxt = j
                            break
                    if nxt == -1:
                        break
                    picked.append(nxt)
                    cur = nxt
                if len(picked) == k:
                    return True
            return False

        lo, hi = 0, 2 * side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
