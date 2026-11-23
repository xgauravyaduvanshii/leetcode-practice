# LeetCode 3203. Find Minimum Diameter After Merging Two Trees — Hard
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
# Submission 2202078130 — Accepted, Python3
#
# My thinking: merging two trees by one
# edge can only help by joining their
# centres, so the answer is the larger
# of the two diameters and the sum of
# their radii plus one. Each diameter
# comes from two BFS sweeps: the farthest
# node from anywhere is one end of a
# diameter.

from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        from collections import deque

        def diameter(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)

            def farthest(start):
                dist = [-1] * n
                dist[start] = 0
                dq = deque([start])
                far = start
                while dq:
                    u = dq.popleft()
                    far = u
                    for v in adj[u]:
                        if dist[v] == -1:
                            dist[v] = dist[u] + 1
                            dq.append(v)
                return far, dist[far]

            a, _ = farthest(0)
            _, d = farthest(a)
            return d

        d1 = diameter(edges1)
        d2 = diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
