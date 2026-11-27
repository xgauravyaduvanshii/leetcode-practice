# LeetCode 2368. Reachable Nodes With Restrictions — Medium
# https://leetcode.com/problems/reachable-nodes-with-restrictions/
# Submission 2204751445 — Accepted, Python3
#
# My thinking: build the adjacency list, then walk from node 0 with a
# stack, never stepping onto a restricted node and never revisiting a
# node. Every node reached this way is reachable without passing a
# restricted node, and no other node is — the count of visited nodes is
# the answer.
class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        banned = set(restricted)
        seen = {0}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen and v not in banned:
                    seen.add(v)
                    stack.append(v)
        return len(seen)
