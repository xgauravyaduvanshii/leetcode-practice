# LeetCode 2360. Longest Cycle in a Graph — Hard
# https://leetcode.com/problems/longest-cycle-in-a-graph/
# Submission 2201698495 — Accepted, Python3
#
# My thinking: every node points to at
# most one next node, so I walk each chain
# once, stamping when I first meet a node
# — meeting one again inside the same walk
# is a cycle, and its length is how far I
# have come since that stamp.

class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        visited = [False] * n
        ans = -1
        for start in range(n):
            if visited[start]:
                continue
            step = {}
            u = start
            s = 0
            while u != -1 and not visited[u]:
                if u in step:
                    ans = max(ans, s - step[u])
                    break
                step[u] = s
                s += 1
                u = edges[u]
            for node in step:
                visited[node] = True
        return ans
