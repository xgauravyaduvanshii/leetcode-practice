# LeetCode 2493. Divide Nodes Into the Maximum Number of Groups — Hard
# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
# Submission 2201778322 — Accepted, Python3
#
# My thinking: neighbours must sit in
# groups exactly one apart, so each
# connected piece has to be bipartite —
# an odd cycle makes the whole thing
# impossible — and the most groups a piece
# can take is its longest shortest path
# plus one, which I find by walking out
# from every node in the piece.

from collections import deque


class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            a -= 1
            b -= 1
            adj[a].append(b)
            adj[b].append(a)

        def bfs(start):
            dist = {start: 0}
            q = deque([start])
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if w not in dist:
                        dist[w] = dist[u] + 1
                        q.append(w)
            return dist

        seen = [False] * n
        total = 0
        for s in range(n):
            if seen[s]:
                continue
            comp = bfs(s)
            for v in comp:
                seen[v] = True
            # bipartite check: colour by BFS depth parity
            colour = {}
            for v in comp:
                colour[v] = comp[v] % 2
            for v in comp:
                for w in adj[v]:
                    if colour[v] == colour[w]:
                        return -1
            best = 0
            for v in comp:
                d = bfs(v)
                best = max(best, max(d.values()))
            total += best + 1
        return total
