# LeetCode 1857. Largest Color Value in a Directed Graph — Hard
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
# Submission 2201204546 — Accepted, Python3
#
# My thinking: I walk the graph in topological
# order, carrying for every node the best count
# of each colour on any path reaching it — if
# some node is never reached the graph has a
# cycle and the answer is minus one.

from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
        dp = [[0] * 26 for _ in range(n)]
        q = deque([i for i in range(n) if indeg[i] == 0])
        seen = 0
        ans = 0
        while q:
            u = q.popleft()
            seen += 1
            dp[u][ord(colors[u]) - 97] += 1
            ans = max(ans, max(dp[u]))
            for v in graph[u]:
                for c in range(26):
                    if dp[u][c] > dp[v][c]:
                        dp[v][c] = dp[u][c]
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return -1 if seen < n else ans
