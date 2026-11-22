# LeetCode 2685. Count the Number of Complete Components — Medium
# https://leetcode.com/problems/count-the-number-of-complete-components/
# Submission 2200899058 — Accepted, Python3
#
# My thinking: inside each connected component, every node
# must be linked to every other one — so I count a
# component only when its edge count matches the full
# triangle number for its size.

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            parent[find(u)] = find(v)
        size = {}
        edge_count = {}
        for i in range(n):
            root = find(i)
            size[root] = size.get(root, 0) + 1
        for u, v in edges:
            edge_count[find(u)] = edge_count.get(find(u), 0) + 1
        return sum(
            1 for root, count in size.items()
            if edge_count.get(root, 0) == count * (count - 1) // 2
        )
