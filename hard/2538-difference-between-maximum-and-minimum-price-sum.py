# LeetCode 2538. Difference Between Maximum and Minimum Price Sum — Hard
# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/
# Submission 2201804020 — Accepted, Python3
#
# My thinking: from any root the
# cheapest path is the root alone, so
# the cost is just the dearest path
# starting there minus the root's own
# price — I learn the best downward
# walk from every node and the best walk
# coming in from above, then take the
# widest gap.

import sys
sys.setrecursionlimit(300000)


class Solution:
    def maxOutput(self, n: int, edges: list[list[int]], price: list[int]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        down = [0] * n
        up = [0] * n
        parent = [-1] * n
        order = [0]
        parent[0] = -2
        for u in order:
            for w in adj[u]:
                if parent[w] == -1:
                    parent[w] = u
                    order.append(w)
        for u in reversed(order):
            best = 0
            for w in adj[u]:
                if parent[w] == u:
                    best = max(best, down[w])
            down[u] = price[u] + best
        for u in order:
            # best two downward contributions among the children
            top1 = top2 = 0
            for w in adj[u]:
                if parent[w] == u:
                    if down[w] > top1:
                        top2, top1 = top1, down[w]
                    elif down[w] > top2:
                        top2 = down[w]
            for w in adj[u]:
                if parent[w] == u:
                    use = top1 if down[w] != top1 else top2
                    up[w] = price[w] + max(up[u], price[u] + use)
        ans = 0
        for u in range(n):
            best_path = max(down[u], up[u])
            ans = max(ans, best_path - price[u])
        return ans
