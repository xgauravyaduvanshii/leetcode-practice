# LeetCode 1697. Checking Existence of Edge Length Limited Paths — Hard
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
# Submission 2201097788 — Accepted, Python3
#
# My thinking: I sort the edges and the queries by
# their limits, then sweep through adding edges to a
# union-find as their weight becomes allowed — a query
# is answered by whether its two ends are already
# connected when its limit is reached.

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        edgeList.sort(key=lambda e: e[2])
        order = sorted(range(len(queries)), key=lambda i: queries[i][2])
        answer = [False] * len(queries)
        e = 0
        for i in order:
            p, q, limit = queries[i]
            while e < len(edgeList) and edgeList[e][2] < limit:
                union(edgeList[e][0], edgeList[e][1])
                e += 1
            answer[i] = find(p) == find(q)
        return answer
