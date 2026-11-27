# LeetCode 2065. Maximum Path Quality of a Graph — Hard
# https://leetcode.com/problems/maximum-path-quality-of-a-graph/
# Submission 2200895875 — Accepted, Python3
#
# My thinking: I walk every route from node 0 and back,
# counting each node's value only the first time I visit
# it, and keep the best total that still returns in time.

class Solution:
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        graph = [[] for _ in range(len(values))]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        visited = [0] * len(values)
        visited[0] = 1
        best = [values[0]]

        def dfs(node: int, time_left: int, total: int) -> None:
            if node == 0:
                best[0] = max(best[0], total)
            for nxt, t in graph[node]:
                if t <= time_left:
                    first = visited[nxt] == 0
                    visited[nxt] += 1
                    dfs(nxt, time_left - t, total + (values[nxt] if first else 0))
                    visited[nxt] -= 1

        dfs(0, maxTime, values[0])
        return best[0]
