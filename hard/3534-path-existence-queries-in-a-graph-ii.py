# LeetCode 3534. Path Existence Queries in a Graph II — Hard
# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
# Submission 2202813515 — Accepted, Python3
from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # My thinking: two nodes are joined when their values differ
        # by at most maxDiff, so after sorting by value the graph
        # becomes a chain of intervals — a node reaches exactly the
        # nodes whose values lie within maxDiff of it. The cheapest
        # way across is to always jump to the farthest value still
        # within reach, and that greedy jump is a function on sorted
        # positions, so binary lifting counts how many jumps a query
        # needs. A gap wider than maxDiff between neighbours splits
        # the components, and then the answer is -1.
        order = sorted(range(n), key=lambda i: nums[i])
        vals = [nums[i] for i in order]
        pos = [0] * n
        for p, idx in enumerate(order):
            pos[idx] = p
        go = [0] * n
        r = 0
        for i in range(n):
            if r < i:
                r = i
            while r + 1 < n and vals[r + 1] - vals[i] <= maxDiff:
                r += 1
            go[i] = r
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid
        LOG = 18
        up = [go[:]]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])
        ans = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            if pu == pv:
                ans.append(0)
                continue
            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue
            if pu > pv:
                pu, pv = pv, pu
            cur = pu
            t = 0
            for kk in range(LOG - 1, -1, -1):
                if up[kk][cur] < pv:
                    cur = up[kk][cur]
                    t += 1 << kk
            ans.append(t + 1)
        return ans
