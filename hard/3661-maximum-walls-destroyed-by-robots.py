# LeetCode 3661. Maximum Walls Destroyed by Robots — Hard
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/
# Submission 2203019845 — Accepted, Python3
import bisect
from typing import List


class Solution:
    def maxWallsDestroyedByRobots(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # My thinking: sort the robots by position, then each robot
        # only ever interacts with its immediate neighbours — a shot
        # to the left is blocked by the robot on its left, a shot to
        # the right by the robot on its right, so the only walls two
        # robots can both hit are the ones between them when they
        # fire towards each other. I count, for every robot, how
        # many walls its left shot and its right shot each destroy,
        # plus the overlap between neighbours, and run a two-state
        # DP (this robot fires left / right), subtracting the
        # overlap only when neighbours fire towards each other.
        pairs = sorted(zip(robots, distance))
        pos = [p for p, _ in pairs]
        dist = [d for _, d in pairs]
        w = sorted(walls)
        n = len(pos)

        def count(lo: int, hi: int) -> int:
            if lo > hi:
                return 0
            return bisect.bisect_right(w, hi) - bisect.bisect_left(w, lo)

        left = [0] * n
        right = [0] * n
        for i in range(n):
            lo = pos[i] - dist[i] if i == 0 else max(pos[i] - dist[i], pos[i - 1] + 1)
            left[i] = count(lo, pos[i])
            hi = pos[i] + dist[i] if i == n - 1 else min(pos[i] + dist[i], pos[i + 1] - 1)
            right[i] = count(pos[i], hi)
        overlap = [0] * max(0, n - 1)
        for i in range(n - 1):
            overlap[i] = count(max(pos[i + 1] - dist[i + 1], pos[i] + 1),
                              min(pos[i] + dist[i], pos[i + 1] - 1))
        dp_left, dp_right = left[0], right[0]
        for i in range(1, n):
            ndp_left = max(dp_left, dp_right - overlap[i - 1]) + left[i]
            ndp_right = max(dp_left, dp_right) + right[i]
            dp_left, dp_right = ndp_left, ndp_right
        return max(dp_left, dp_right)
