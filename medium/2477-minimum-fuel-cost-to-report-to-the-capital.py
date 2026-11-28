# LeetCode 2477. Minimum Fuel Cost to Report to the Capital — Medium
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
# Submission 2204968007 — Accepted, Python3
#
# My thinking: root the tree at the capital. Every subtree's people
# must travel up through their parent edge together, so that edge
# costs ceil(subtree size / seats) litres of fuel. Add that up for
# every non-root node.
class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = [[] for _ in range(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        parent = [-1] * n
        parent[0] = -2
        order = [0]
        for u in order:
            for w in adj[u]:
                if parent[w] == -1:
                    parent[w] = u
                    order.append(w)
        size = [1] * n
        fuel = 0
        for u in reversed(order):
            if u == 0:
                continue
            fuel += (size[u] + seats - 1) // seats
            size[parent[u]] += size[u]
        return fuel
