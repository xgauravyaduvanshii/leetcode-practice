# LeetCode 3241. Time Taken to Mark All Nodes — Hard
# https://leetcode.com/problems/time-taken-to-mark-all-nodes/
# Submission 2202123321 — Accepted, Python3
#
# My thinking: moving into a node costs 1 if
# the node is odd and 2 if it is even, so the
# time from a start node is the most expensive
# root-to-leaf walk in any direction. I root
# the tree at 0 and compute down values bottom
# up (best walk inside the subtree) and up
# values top down (best walk outside it, using
# the top two sibling branches), then each
# answer is max(down, up).

from typing import List


class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = -2
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)
        down = [0] * n
        for u in reversed(order):
            best = 0
            for v in adj[u]:
                if v == parent[u]:
                    continue
                cand = (1 if v & 1 else 2) + down[v]
                if cand > best:
                    best = cand
            down[u] = best
        up = [0] * n
        for u in order:
            top1 = 0
            top2 = 0
            cnt1 = 0
            for v in adj[u]:
                if v == parent[u]:
                    continue
                cand = (1 if v & 1 else 2) + down[v]
                if cand > top1:
                    top2 = top1
                    top1 = cand
                    cnt1 = 1
                elif cand == top1:
                    cnt1 += 1
                elif cand > top2:
                    top2 = cand
            cost_u = 1 if u & 1 else 2
            for v in adj[u]:
                if v == parent[u]:
                    continue
                cand = (1 if v & 1 else 2) + down[v]
                if cand < top1 or cnt1 >= 2:
                    sibling = top1
                else:
                    sibling = top2
                best_excl = up[u]
                if sibling > best_excl:
                    best_excl = sibling
                up[v] = cost_u + best_excl
        return [down[i] if down[i] > up[i] else up[i] for i in range(n)]
