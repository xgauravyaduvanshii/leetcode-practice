# LeetCode 4023. Elevator Requests II — Hard
# https://leetcode.com/problems/elevator-requests-ii/
# Submission 2203514444 — Accepted, Python3
from typing import List


class Solution:
    def elevatorRequests(self, n: int, start: int, requests: List[int]) -> int:
        # My thinking: only the relative order of the
        # requested floors matters, so sort them and add
        # the start floor. At any moment the visited
        # floors form one contiguous interval around the
        # start, because the elevator never gains by
        # passing an unvisited floor. Moving to the next
        # unvisited floor on either side costs the
        # distance times the number of requests still
        # unfulfilled — every one of them waits through
        # the whole move, including the destination.
        # dp over intervals [l, r] with the elevator at
        # the left or right end is therefore enough, and
        # only the current interval length needs storing:
        # each step expands the interval by one floor on
        # either side. The answer is the cheaper of the
        # two ways to finish with the whole interval
        # visited.
        pts = sorted(set(requests) | {start})
        m = len(pts)
        s = pts.index(start)
        inf = 10 ** 30
        dp0 = [inf] * m
        dp1 = [inf] * m
        dp0[s] = 0
        dp1[s] = 0
        for length in range(1, m):
            ndp0 = [inf] * m
            ndp1 = [inf] * m
            rem = m - length
            for l in range(0, m - length + 1):
                r = l + length - 1
                if not l <= s <= r:
                    continue
                c = dp0[l]
                if c < inf:
                    if l > 0:
                        v = c + (pts[l] - pts[l - 1]) * rem
                        if v < ndp0[l - 1]:
                            ndp0[l - 1] = v
                    if r + 1 < m:
                        v = c + (pts[r + 1] - pts[l]) * rem
                        if v < ndp1[l]:
                            ndp1[l] = v
                c = dp1[l]
                if c < inf:
                    if l > 0:
                        v = c + (pts[r] - pts[l - 1]) * rem
                        if v < ndp0[l - 1]:
                            ndp0[l - 1] = v
                    if r + 1 < m:
                        v = c + (pts[r + 1] - pts[r]) * rem
                        if v < ndp1[l]:
                            ndp1[l] = v
            dp0, dp1 = ndp0, ndp1
        return min(dp0[0], dp1[0])
