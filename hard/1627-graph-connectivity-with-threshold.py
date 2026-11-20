class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        # My thinking: two numbers link when they share a
        # divisor bigger than the threshold — so join every
        # multiple of each big divisor and read the answers off.
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        for d in range(threshold + 1, n + 1):
            for m in range(d * 2, n + 1, d):
                union(d, m)
        return [find(a) == find(b) for a, b in queries]
