# LeetCode 4100. Minimum Cost Path With Even XOR Parity — Hard
# https://leetcode.com/problems/minimum-cost-path-with-even-xor-parity/
# Submission 2203731883 — Accepted, Python3
class Solution:
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
        # My thinking: the XOR of a path has an even
        # number of set bits exactly when the number of
        # nodes on the path whose value has odd parity
        # (odd number of set bits) is even. So a path
        # is Balanced-XOR when it contains an even
        # count of parity-1 nodes. Any single edge
        # joining two nodes of equal parity has zero
        # parity-1 nodes on its two endpoints, so it
        # is already balanced — the cheapest such edge
        # is a candidate answer. Otherwise a balanced
        # path needs at least two parity-1 nodes, and
        # the cheapest such path has exactly two edges:
        # 1 - 0 - 1, going through a parity-0 middle
        # node. For each parity-0 node, keep its two
        # cheapest edges to parity-1 neighbors; their
        # sum is the cheapest 1-0-1 path through it.
        # The answer is the smaller of the cheapest
        # balanced edge and the cheapest 1-0-1 path,
        # or -1 when neither exists.
        n = len(values)
        parity = [v.bit_count() & 1 for v in values]
        INF = 10 ** 18
        ans = INF
        best1 = [INF] * n
        best2 = [INF] * n
        for u, v, c in edges:
            if parity[u] == parity[v]:
                if c < ans:
                    ans = c
            if parity[u] == 0 and parity[v] == 1:
                if c < best1[u]:
                    best2[u] = best1[u]
                    best1[u] = c
                elif c < best2[u]:
                    best2[u] = c
            if parity[v] == 0 and parity[u] == 1:
                if c < best1[v]:
                    best2[v] = best1[v]
                    best1[v] = c
                elif c < best2[v]:
                    best2[v] = c
        for i in range(n):
            if parity[i] == 0 and best2[i] < INF:
                s = best1[i] + best2[i]
                if s < ans:
                    ans = s
        return -1 if ans == INF else ans
