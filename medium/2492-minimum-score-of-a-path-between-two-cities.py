# LeetCode 2492. Minimum Score of a Path Between Two Cities — Medium
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# Submission 2200896566 — Accepted, Python3
#
# My thinking: any road I can reach from city 1 while
# staying connected to city n is usable, so I walk the
# whole reachable component and take its smallest road.

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        seen = {1}
        stack = [1]
        best = float("inf")
        while stack:
            node = stack.pop()
            for nxt, d in graph[node]:
                best = min(best, d)
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return best
