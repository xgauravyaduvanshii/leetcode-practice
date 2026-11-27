# LeetCode 3772. Maximum Subgraph Score in a Tree — Hard
# https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/
# Submission 2203170869 — Accepted, Python3
from typing import List


class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        # My thinking: give each node the value +1 if good and
        # -1 if bad, so a subgraph's score is the sum of its
        # nodes' values. Root the tree anywhere and first work
        # bottom-up: down[u] is the best connected subgraph
        # containing u and staying inside u's subtree, which
        # takes u plus every child subtree whose down value is
        # positive. Then work top-down (rerooting): for a child
        # v of u, the best piece of the rest of the tree that
        # can hang off u is u's value plus the positive child
        # contributions except v's, plus u's own parent-side
        # piece when positive. The answer for u is its value
        # plus every positive contribution from all sides.
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        val = [1 if g else -1 for g in good]

        parent = [-1] * n
        parent[0] = -2
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for w in adj[u]:
                if parent[w] == -1:
                    parent[w] = u
                    stack.append(w)

        down = val[:]
        for u in reversed(order):
            for w in adj[u]:
                if parent[w] == u and down[w] > 0:
                    down[u] += down[w]

        # up[u] is the value of the best connected piece that
        # contains u's parent but no node of u's subtree; it
        # is only ever added when positive, so it may be
        # negative here and that is fine.
        up = [0] * n
        ans = [0] * n
        for u in order:
            total = val[u]
            if up[u] > 0:
                total += up[u]
            children = [w for w in adj[u] if parent[w] == u]
            pos = [down[w] if down[w] > 0 else 0 for w in children]
            total += sum(pos)
            ans[u] = total
            # Prefix sums over the positive child contributions
            # give each child the sum of its siblings' in O(1).
            pref = [0] * (len(children) + 1)
            for i, p in enumerate(pos):
                pref[i + 1] = pref[i] + p
            rest = val[u] + (up[u] if up[u] > 0 else 0)
            for i, v in enumerate(children):
                up[v] = rest + (pref[-1] - pos[i])
        return ans
