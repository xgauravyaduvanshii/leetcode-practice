# LeetCode 2699. Modify Graph Edge Weights — Hard
# https://leetcode.com/problems/modify-graph-edge-weights/
# Submission 2201871288 — Accepted, Python3
#
# My thinking: if the fixed roads
# alone already beat the target there
# is nothing to do, and if the cheapest
# road with every -1 set to 1 already
# overshoots, it can never be done — so
# I take the cheapest road, stretch one
# of its -1 edges until that road is
# exactly the target, price every -1
# that is not on that road out of the
# way, and check the road really
# measures the target.

import heapq


class Solution:
    def modifiedGraphEdges(self, n: int, edges: list[list[int]], source: int, destination: int, target: int) -> list[list[int]]:
        def dijkstra(adj, src):
            dist = [float("inf")] * n
            prev = [-1] * n
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for v, w, ei in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        prev[v] = (u, ei)
                        heapq.heappush(pq, (nd, v))
            return dist, prev

        def build(weights):
            adj = [[] for _ in range(n)]
            for ei, (a, b, w) in enumerate(edges):
                wt = weights[ei]
                adj[a].append((b, wt, ei))
                adj[b].append((a, wt, ei))
            return adj

        neg = [ei for ei, (_, _, w) in enumerate(edges) if w == -1]
        # cheapest road with every -1 set to 1
        w1 = [w if w > 0 else 1 for _, _, w in edges]
        adj1 = build(w1)
        d1, prev = dijkstra(adj1, source)
        if d1[destination] > target:
            return []
        if d1[destination] == target:
            return [[a, b, w if w > 0 else 1] for a, b, w in edges]
        # reconstruct the cheapest road and its -1 edges
        path_edges = []
        cur = destination
        while cur != source and prev[cur] != -1:
            u, ei = prev[cur]
            path_edges.append(ei)
            cur = u
        if cur != source:
            return []
        path_neg = [ei for ei in path_edges if edges[ei][2] == -1]
        if not path_neg:
            return []
        # fixed-only roads must not already beat the target
        fixed_adj = [[] for _ in range(n)]
        for ei, (a, b, w) in enumerate(edges):
            if w > 0:
                fixed_adj[a].append((b, w, ei))
                fixed_adj[b].append((a, w, ei))
        d_fixed, _ = dijkstra(fixed_adj, source)
        if d_fixed[destination] < target:
            return []
        on_path = set(path_edges)
        for adjust in path_neg:
            extra = target - d1[destination]
            weights = []
            for ei, (a, b, w) in enumerate(edges):
                if w > 0:
                    weights.append(w)
                elif ei == adjust:
                    weights.append(1 + extra)
                elif ei in on_path:
                    weights.append(1)
                else:
                    weights.append(2000000000)
            adj = build(weights)
            if dijkstra(adj, source)[0][destination] == target:
                return [[a, b, weights[ei]] for ei, (a, b, _) in enumerate(edges)]
        return []
