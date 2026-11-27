import heapq


class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        # My thinking: run Dijkstra from node 0, then every edge
        # contributes the subdivided nodes reachable from either end
        # within the remaining moves.
        graph = [[] for _ in range(n)]
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))
        dist = [float("inf")] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))
        reachable = sum(1 for d in dist if d <= maxMoves)
        for u, v, cnt in edges:
            left = max(0, maxMoves - dist[u]) if dist[u] <= maxMoves else 0
            right = max(0, maxMoves - dist[v]) if dist[v] <= maxMoves else 0
            reachable += min(cnt, left + right)
        return reachable
