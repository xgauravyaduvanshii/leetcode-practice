# LeetCode 3515. Shortest Path in a Weighted Tree — Hard
# https://leetcode.com/problems/shortest-path-in-a-weighted-tree/
# Submission 2202788546 — Accepted, Python3
from typing import List
from collections import defaultdict


class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # My thinking: in a tree the distance from the root to any node
        # is just the sum of the edge weights on the root-to-node path.
        # Updating one edge only changes the distance of the nodes in
        # that edge's subtree (the deeper endpoint's side), so I turn
        # each edge update into a range add over the subtree (Euler
        # tour times give every subtree a contiguous interval) and
        # answer a query by adding the accumulated delta to the
        # node's initial root distance. A Fenwick tree does the range
        # add / point query in O(log n).
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        parent = [0] * (n + 1)
        dist0 = [0] * (n + 1)
        timer = 0
        stack = [(1, 0, 0)]
        while stack:
            node, par, state = stack.pop()
            if state == 0:
                timer += 1
                tin[node] = timer
                parent[node] = par
                stack.append((node, par, 1))
                for nb, w in adj[node]:
                    if nb == par:
                        continue
                    dist0[nb] = dist0[node] + w
                    stack.append((nb, node, 0))
            else:
                tout[node] = timer
        size = n + 2
        bit = [0] * (size + 1)

        def bit_add(i, delta):
            while i <= size:
                bit[i] += delta
                i += i & -i

        def bit_sum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def range_add(l, r, delta):
            bit_add(l, delta)
            bit_add(r + 1, -delta)

        cur_w = {}
        for u, v, w in edges:
            child = v if parent[v] == u else u
            cur_w[child] = w
        ans = []
        for q in queries:
            if q[0] == 1:
                _, u, v, w = q
                child = v if parent[v] == u else u
                delta = w - cur_w[child]
                cur_w[child] = w
                range_add(tin[child], tout[child], delta)
            else:
                _, x = q
                ans.append(dist0[x] + bit_sum(tin[x]))
        return ans
