# LeetCode 2467. Most Profitable Path in a Tree — Medium
# https://leetcode.com/problems/most-profitable-path-in-a-tree/
# Submission 2204963048 — Accepted, Python3
#
# My thinking: Bob walks straight from his start to the root, so
# record his arrival time at each node on that path. Alice walks
# from the root down; at each node she takes the full amount if she
# arrives before Bob, half if they arrive together, and nothing if
# Bob was there first. The best root-to-leaf total is the answer.
class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n = len(amount)
        adj = [[] for _ in range(n)]
        for u, v in edges:
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
        bob_time = {}
        node = bob
        t = 0
        while node != -2:
            bob_time[node] = t
            t += 1
            node = parent[node]
        best = float("-inf")
        stack = [(0, -1, 0, 0)]
        while stack:
            u, par, time, income = stack.pop()
            bt = bob_time.get(u, float("inf"))
            if time < bt:
                income += amount[u]
            elif time == bt:
                income += amount[u] // 2
            if u != 0 and len(adj[u]) == 1:
                if income > best:
                    best = income
            for w in adj[u]:
                if w != par:
                    stack.append((w, u, time + 1, income))
        return best
