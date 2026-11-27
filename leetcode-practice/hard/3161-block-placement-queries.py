# LeetCode 3161. Block Placement Queries — Hard
# https://leetcode.com/problems/block-placement-queries/
# Submission 2202050726 — Accepted, Python3
#
# My thinking: a query asks whether some
# gap between consecutive obstacles,
# starting at or before x - sz, is at
# least sz wide. I keep the gaps in a
# sqrt-decomposed array for range-maximum
# queries and the obstacles in
# sqrt-decomposed sorted blocks, so
# inserting an obstacle updates just the
# two gaps it splits and each query is
# answered from the biggest gap seen so
# far.

from bisect import bisect_left, bisect_right, insort
from typing import List


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        INF = 10 ** 9
        xs = sorted({q[1] for q in queries if q[0] == 1})
        comp = [0] + xs
        idx_of = {v: i for i, v in enumerate(comp)}
        M = len(comp)
        B = 450
        nb = (M + B - 1) // B
        gap = [0] * M
        gap[0] = INF
        bmax = [0] * nb
        for b in range(nb):
            bmax[b] = max(gap[b * B:(b + 1) * B])

        def point_update(idx, val):
            gap[idx] = val
            b = idx // B
            bmax[b] = max(gap[b * B:min((b + 1) * B, M)])

        def prefix_max(idx):
            if idx < 0:
                return 0
            b = idx // B
            res = 0
            if b > 0:
                res = max(bmax[:b])
            part = max(gap[b * B:idx + 1])
            return res if res > part else part

        SB = 700
        blocks = [[]]
        tops = []

        def obs_pred(x):
            if not tops:
                return None
            i = bisect_left(tops, x)
            if i >= len(blocks):
                return blocks[-1][-1]
            block = blocks[i]
            j = bisect_left(block, x)
            if j > 0:
                return block[j - 1]
            if i > 0:
                return blocks[i - 1][-1]
            return None

        def obs_succ(x):
            if not tops:
                return None
            i = bisect_right(tops, x)
            if i >= len(blocks):
                return None
            block = blocks[i]
            j = bisect_right(block, x)
            if j < len(block):
                return block[j]
            if i + 1 < len(blocks):
                return blocks[i + 1][0]
            return None

        def obs_add(x):
            if not tops:
                blocks[0].append(x)
                tops.append(x)
                return
            i = bisect_right(tops, x)
            if i >= len(blocks):
                i = len(blocks) - 1
            block = blocks[i]
            insort(block, x)
            tops[i] = block[-1]
            if len(block) > 2 * SB:
                mid = len(block) // 2
                new_block = block[mid:]
                del block[mid:]
                blocks.insert(i + 1, new_block)
                tops[i] = block[-1]
                tops.insert(i + 1, new_block[-1])

        res = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                pred = obs_pred(x)
                succ = obs_succ(x)
                left_pos = pred if pred is not None else 0
                point_update(idx_of[left_pos], x - left_pos)
                point_update(idx_of[x], (succ - x) if succ is not None else INF)
                obs_add(x)
            else:
                x, sz = q[1], q[2]
                X = x - sz
                if X < 0:
                    res.append(False)
                else:
                    idx = bisect_right(comp, X) - 1
                    res.append(prefix_max(idx) >= sz)
        return res
