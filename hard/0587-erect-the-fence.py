# LeetCode 587. Erect the Fence — Hard
# https://leetcode.com/problems/erect-the-fence/
# Submission 2198664146 — Accepted, Python3
#
# My thinking: the fence is the convex hull, built
# with a monotone chain — one pass left to right for
# the lower hull, one pass right to left for the upper.
# I only pop on a right turn, so points lying flat on
# an edge stay in the answer, which is what the
# problem wants.

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        points = sorted(set(map(tuple, trees)))
        if len(points) <= 1:
            return [list(p) for p in points]

        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
        return [list(p) for p in set(lower + upper)]
