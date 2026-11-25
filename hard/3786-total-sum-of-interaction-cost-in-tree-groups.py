# LeetCode 3786. Total Sum of Interaction Cost in Tree Groups — Hard
# https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/
# Submission 2203179188 — Accepted, Python3
import numpy as np
from typing import List


class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        # My thinking: the distance between two same-group nodes
        # is the number of tree edges on their path, so each edge
        # contributes once for every same-group pair whose path
        # crosses it. Root the tree at 0: for the edge down to a
        # child subtree, a group with cnt nodes inside the
        # subtree and total - cnt outside contributes
        # cnt * (total - cnt). There are only 20 groups, so one
        # bottom-up pass keeps a 21-wide count vector per
        # subtree — numpy adds make the per-edge work cheap —
        # and adds each edge's contribution with one dot
        # product against the group totals.
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = np.zeros(21, dtype=np.int64)
        for g in group:
            total[g] += 1
        parent = [-1] * n
        parent[0] = -2
        order = [0]
        for u in order:
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    order.append(v)
        sub = np.zeros((n, 21), dtype=np.int64)
        ans = 0
        for u in reversed(order):
            row = sub[u]
            for v in adj[u]:
                if parent[v] == u:
                    cv = sub[v]
                    row += cv
                    ans += int(np.dot(cv, total - cv))
            row[group[u]] += 1
        return ans
