from collections import deque


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: list[list[int]]) -> list[int]:
        # My thinking: with at most 15 cities, try every group
        # of them — keep the connected ones and sort them by
        # their widest gap.
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)
        ans = [0] * (n - 1)

        def bfs_farthest(start, nodes):
            dist = {start: 0}
            queue = deque([start])
            while queue:
                x = queue.popleft()
                for y in adj[x]:
                    if y in nodes and y not in dist:
                        dist[y] = dist[x] + 1
                        queue.append(y)
            return dist

        for mask in range(1, 1 << n):
            nodes = {i for i in range(n) if mask >> i & 1}
            if len(nodes) < 2:
                continue
            start = next(iter(nodes))
            dist = bfs_farthest(start, nodes)
            if len(dist) != len(nodes):
                continue
            far = max(dist, key=dist.get)
            dist2 = bfs_farthest(far, nodes)
            d = max(dist2.values())
            ans[d - 1] += 1
        return ans
