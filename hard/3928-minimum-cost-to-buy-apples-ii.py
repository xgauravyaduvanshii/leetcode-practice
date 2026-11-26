# LeetCode 3928. Minimum Cost to Buy Apples II — Hard
# https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/
# Submission 2203423002 — Accepted, Python3
from typing import List

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra


class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        # My thinking: for shop i the cheapest plan is
        # either buying locally, or travelling empty to
        # some shop j, buying there, and carrying the
        # apples back. The forward and return legs may
        # differ, and the graph is undirected, so the
        # empty leg costs the shortest path from i to j
        # in the plain-cost metric and the return leg
        # costs the shortest path from j to i in the
        # cost-times-tax metric. That makes the answer
        # min over j of dist_cost[i][j] + dist_tax[i][j]
        # + prices[j], where the two distance tables are
        # all-pairs shortest paths in the two metrics.
        # A numpy Floyd-Warshall is far too slow here
        # (n up to 1000), so both tables come from
        # scipy's sparse Dijkstra, which runs the
        # all-pairs computation in C from CSR adjacency
        # matrices built once per metric. Unreachable
        # pairs stay infinite and are skipped; the
        # j = i term is just prices[i], so the local
        # purchase is covered automatically.
        def all_pairs(taxed: bool):
            rows, cols, data = [], [], []
            for u, v, c, t in roads:
                w = c * t if taxed else c
                rows.extend((u, v))
                cols.extend((v, u))
                data.extend((w, w))
            graph = csr_matrix((data, (rows, cols)), shape=(n, n))
            return dijkstra(graph, directed=False)

        dist_cost = all_pairs(False)
        dist_tax = all_pairs(True)
        ans = []
        for i in range(n):
            best = prices[i]
            for j in range(n):
                a = dist_cost[i, j]
                b = dist_tax[i, j]
                if np.isfinite(a) and np.isfinite(b):
                    cand = a + b + prices[j]
                    if cand < best:
                        best = cand
            ans.append(int(best))
        return ans
