# LeetCode 850. Rectangle Area II — Hard
# https://leetcode.com/problems/rectangle-area-ii/
# Submission 2198683238 — Accepted, Python3
#
# My thinking: I sweep a vertical line from left to
# right, opening each rectangle's y-interval when the
# line reaches its left edge and closing it at its
# right edge. Between two events the covered height
# stays fixed, so the strip's area is its width times
# the merged height of the open intervals.

from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 1))
            events.append((x2, y1, y2, -1))
        events.sort()
        active = []
        area = 0
        prev_x = events[0][0]
        for x, y1, y2, kind in events:
            width = x - prev_x
            if width and active:
                merged = sorted(active)
                covered = 0
                start, end = merged[0]
                for a, b in merged[1:]:
                    if a > end:
                        covered += end - start
                        start, end = a, b
                    else:
                        end = max(end, b)
                covered += end - start
                area += width * covered
            if kind == 1:
                active.append((y1, y2))
            else:
                active.remove((y1, y2))
            prev_x = x
        return area % MOD
