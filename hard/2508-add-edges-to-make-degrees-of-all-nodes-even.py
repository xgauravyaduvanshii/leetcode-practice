# LeetCode 2508. Add Edges to Make Degrees of All Nodes Even — Hard
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/
# Submission 2200895651 — Accepted, Python3
#
# My thinking: I count the odd-degree nodes — there can
# only be 0, 2 or 4 of them — then check whether one or
# two new edges can fix them without duplicating an
# existing edge.

class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        graph = [set() for _ in range(n + 1)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        odd = [i for i in range(1, n + 1) if len(graph[i]) % 2 == 1]
        if not odd:
            return True
        if len(odd) == 2:
            a, b = odd
            if b not in graph[a]:
                return True
            for c in range(1, n + 1):
                if c != a and c != b and a not in graph[c] and b not in graph[c]:
                    return True
            return False
        if len(odd) == 4:
            a, b, c, d = odd
            return (
                (b not in graph[a] and d not in graph[c])
                or (c not in graph[a] and d not in graph[b])
                or (d not in graph[a] and c not in graph[b])
            )
        return False
