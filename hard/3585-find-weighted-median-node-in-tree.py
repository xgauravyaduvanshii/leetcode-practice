# LeetCode 3585. Find Weighted Median Node in Tree — Hard
# https://leetcode.com/problems/find-weighted-median-node-in-tree/
# Submission 2202862360 — Accepted, Python3
from typing import List


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # My thinking: the median is the first node on the path
        # from u whose distance from u reaches half the total path
        # weight. I work with doubled distances so I never touch a
        # float. If the climb to the lowest common ancestor already
        # reaches half, I lift up from u as far as I can while
        # staying under half and take one more step; otherwise the
        # median is on the way down, and I lift up from v as far as
        # the remaining budget allows, which lands on it directly.
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        LOG = 18
        up = [[-1] * n for _ in range(LOG)]
        wsum = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n
        parent = [-1] * n
        order = [0]
        parent[0] = -2
        for u in order:
            for v, w in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    up[0][v] = u
                    wsum[0][v] = w
                    order.append(v)
        up[0][0] = 0
        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]
                wsum[k][i] = wsum[k - 1][i] + wsum[k - 1][up[k - 1][i]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        def jump_up_lt(cur, limit2):
            acc = 0
            for k in range(LOG - 1, -1, -1):
                anc = up[k][cur]
                if anc != -1 and 2 * (acc + wsum[k][cur]) < limit2:
                    acc += wsum[k][cur]
                    cur = anc
            return cur

        def jump_up_le(cur, limit2):
            acc = 0
            for k in range(LOG - 1, -1, -1):
                anc = up[k][cur]
                if anc != -1 and 2 * (acc + wsum[k][cur]) <= limit2:
                    acc += wsum[k][cur]
                    cur = anc
            return cur

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(u)
                continue
            w = lca(u, v)
            du = dist[u] - dist[w]
            dv = dist[v] - dist[w]
            W = du + dv
            if 2 * du >= W:
                cur = jump_up_lt(u, W)
                ans.append(up[0][cur])
            else:
                limit2 = 2 * dv - W + 2 * du
                ans.append(jump_up_le(v, limit2))
        return ans
