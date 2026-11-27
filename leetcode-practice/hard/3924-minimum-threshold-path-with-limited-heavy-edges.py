# LeetCode 3924. Minimum Threshold Path With Limited Heavy Edges — Hard
# https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/
# Submission 2203405476 — Accepted, Python3
from collections import deque
from typing import List


class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        # My thinking: for a fixed threshold T an edge is
        # heavy exactly when its weight is above T, so a
        # path is valid when it uses at most k heavy edges.
        # That is a shortest path in a 0-1 graph — light
        # edges cost 0, heavy edges cost 1 — solved with
        # a 0-1 BFS. Validity is monotone in T: raising
        # the threshold only turns heavy edges light, so
        # the smallest valid threshold is found by binary
        # search over the candidate values 0 and the
        # distinct edge weights (nothing changes between
        # consecutive weights). If even the largest weight
        # fails, the target is unreachable and the answer
        # is -1. Source equal to target needs no edges,
        # so threshold 0 works.
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def valid(threshold: int) -> bool:
            inf = 10 ** 9
            dist = [inf] * n
            dist[source] = 0
            dq = deque([source])
            while dq:
                u = dq.popleft()
                for v, w in adj[u]:
                    c = 1 if w > threshold else 0
                    if dist[u] + c < dist[v]:
                        dist[v] = dist[u] + c
                        if c == 0:
                            dq.appendleft(v)
                        else:
                            dq.append(v)
            return dist[target] <= k

        candidates = sorted({0} | {w for _, _, w in edges})
        if not valid(candidates[-1]):
            return -1
        lo, hi = 0, len(candidates) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if valid(candidates[mid]):
                hi = mid
            else:
                lo = mid + 1
        return candidates[lo]
