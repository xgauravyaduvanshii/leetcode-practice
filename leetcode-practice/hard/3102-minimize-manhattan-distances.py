# LeetCode 3102. Minimize Manhattan Distances — Hard
# https://leetcode.com/problems/minimize-manhattan-distances/
# Submission 2201993237 — Accepted, Python3
#
# My thinking: in (x + y, x - y)
# coordinates the Manhattan distance is
# the larger of the two coordinate gaps.
# Removing one point can only shrink
# the answer if that point is an extreme
# in either coordinate, so I only try
# removing the two smallest and two
# largest in each — at most eight
# candidates — and keep the best.

from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        u = [x + y for x, y in points]
        v = [x - y for x, y in points]

        def extremes(arr):
            idx = sorted(range(n), key=lambda i: arr[i])
            return idx[:2], idx[-2:]

        min_u, max_u = extremes(u)
        min_v, max_v = extremes(v)
        cand = set(min_u + max_u + min_v + max_v)
        ans = float('inf')
        for i in cand:
            umax = u[max_u[1]] if max_u[1] != i else u[max_u[0]]
            umin = u[min_u[0]] if min_u[0] != i else u[min_u[1]]
            vmax = v[max_v[1]] if max_v[1] != i else v[max_v[0]]
            vmin = v[min_v[0]] if min_v[0] != i else v[min_v[1]]
            ans = min(ans, max(umax - umin, vmax - vmin))
        return int(ans)
