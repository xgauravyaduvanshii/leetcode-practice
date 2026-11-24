# LeetCode 3382. Maximum Area Rectangle With Point Constraints II — Hard
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/
# Submission 2202494127 — Accepted 594/594, Python3
from typing import List


class Solution:
    def maxArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        # My thinking: a valid rectangle's two y's must be neighbours in
        # both of its columns, otherwise a point of that column would sit
        # on its edge, and its two columns must be consecutive occurrences
        # of that y-pair, otherwise a point would sit on its top or bottom
        # edge. So I sweep the columns left to right, remember the last
        # column of each neighbouring y-pair, and keep a segment tree of
        # the last column seen for every y: a candidate is empty exactly
        # when no y between its sides was seen after its left column.
        cols = {}
        for x, y in zip(xCoord, yCoord):
            cols.setdefault(x, []).append(y)
        xs = sorted(cols)
        all_y = sorted({y for y in yCoord})
        yid = {y: i for i, y in enumerate(all_y)}
        size = 1
        while size < len(all_y):
            size *= 2
        tree = [-1] * (2 * size)

        def update(i, v):
            j = i + size
            tree[j] = v
            j //= 2
            while j:
                tree[j] = tree[2 * j] if tree[2 * j] >= tree[2 * j + 1] else tree[2 * j + 1]
                j //= 2

        def query(l, r):
            l += size
            r += size
            best = -1
            while l <= r:
                if l % 2 == 1:
                    best = max(best, tree[l])
                    l += 1
                if r % 2 == 0:
                    best = max(best, tree[r])
                    r -= 1
                l //= 2
                r //= 2
            return best

        pair_last = {}
        ans = -1
        for x in xs:
            ys = sorted(cols[x])
            pairs = [(ys[i], ys[i + 1]) for i in range(len(ys) - 1)]
            for y1, y2 in pairs:
                xp = pair_last.get((y1, y2))
                if xp is not None and query(yid[y1], yid[y2]) <= xp:
                    ans = max(ans, (x - xp) * (y2 - y1))
            for y in ys:
                update(yid[y], x)
            for y1, y2 in pairs:
                pair_last[(y1, y2)] = x
        return ans
