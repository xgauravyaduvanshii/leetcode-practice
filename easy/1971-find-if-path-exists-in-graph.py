# LeetCode 1971. Find if Path Exists in Graph — Easy
# https://leetcode.com/problems/find-if-path-exists-in-graph/
# Submission 2197606627 — Accepted, Python3
#
# My thinking: I build an adjacency list and walk the
# graph from the source with a depth-first search,
# keeping track of the nodes I have already seen.
# If I reach the destination, a path exists.

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = {source}
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nb in graph[node]:
                if nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
        return False
