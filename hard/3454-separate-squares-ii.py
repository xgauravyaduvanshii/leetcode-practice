# LeetCode 3454. Separate Squares II — Hard
# https://leetcode.com/problems/separate-squares-ii/
# Submission 2202548712 — Accepted 763/763, Python3
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # My thinking: sweep a horizontal line upward, keeping
        # the total covered x-length in a segment tree over the
        # compressed x-coordinates, so each strip between two
        # event y's has a known width and area. The first strip
        # whose area reaches half the total union area holds the
        # answer, found by exact integer arithmetic and a single
        # linear interpolation inside that strip.
        xs = sorted({x for x, _, _ in squares} | {x + l for x, _, l in squares})
        pos = {x: i for i, x in enumerate(xs)}
        n = len(xs) - 1  # elementary x-intervals
        cnt = [0] * (4 * max(1, n))
        covered = [0] * (4 * max(1, n))

        def update(node, lo, hi, ql, qr, val):
            if ql > hi or qr < lo:
                return
            if ql <= lo and hi <= qr:
                cnt[node] += val
            else:
                mid = (lo + hi) // 2
                update(node * 2, lo, mid, ql, qr, val)
                update(node * 2 + 1, mid + 1, hi, ql, qr, val)
            if cnt[node] > 0:
                covered[node] = xs[hi + 1] - xs[lo]
            elif lo == hi:
                covered[node] = 0
            else:
                covered[node] = covered[node * 2] + covered[node * 2 + 1]

        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        events.sort()

        stages = []  # (y_start, covered width, y_end)
        total = 0
        for i in range(len(events) - 1):
            y, delta, x1, x2 = events[i]
            if n > 0:
                update(1, 0, n - 1, pos[x1], pos[x2] - 1, delta)
            width = covered[1] if n > 0 else 0
            height = events[i + 1][0] - y
            total += height * width
            stages.append((y, width, events[i + 1][0]))

        below = 0
        for y0, width, y1 in stages:
            area = (y1 - y0) * width
            if 2 * (below + area) >= total:
                if width == 0:
                    return float(y0)
                return y0 + (total - 2 * below) / (2 * width)
            below += area
        return float(events[-1][0])
