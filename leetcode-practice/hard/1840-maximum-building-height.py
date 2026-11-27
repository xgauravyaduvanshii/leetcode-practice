# LeetCode 1840. Maximum Building Height — Hard
# https://leetcode.com/problems/maximum-building-height/
# Submission 2201196310 — Accepted, Python3
#
# My thinking: the first building is height zero
# and every restriction is a ceiling, so I tighten
# the ceilings against their neighbours in both
# directions and take the tallest peak between
# each pair — or past the last one.

class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        pts = [[1, 0]] + [r[:] for r in restrictions]
        pts.sort()
        for i in range(1, len(pts)):
            dist = pts[i][0] - pts[i - 1][0]
            pts[i][1] = min(pts[i][1], pts[i - 1][1] + dist)
        for i in range(len(pts) - 2, -1, -1):
            dist = pts[i + 1][0] - pts[i][0]
            pts[i][1] = min(pts[i][1], pts[i + 1][1] + dist)
        ans = 0
        for i in range(1, len(pts)):
            dist = pts[i][0] - pts[i - 1][0]
            ans = max(ans, (pts[i - 1][1] + pts[i][1] + dist) // 2)
        ans = max(ans, pts[-1][1] + (n - pts[-1][0]))
        return ans
