class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # My thinking: an edge is critical if the cheapest
        # tree without it costs more — and pseudo-critical
        # if a cheapest tree can still be built with it in.
        indexed = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        indexed.sort()

        def mst_weight(skip=-1, force=-1):
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            total = 0
            used = 0
            if force != -1:
                u, v, w = edges[force]
                ru, rv = find(u), find(v)
                parent[ru] = rv
                total += w
                used += 1
            for w, u, v, i in indexed:
                if i == skip or i == force:
                    continue
                ru, rv = find(u), find(v)
                if ru != rv:
                    parent[ru] = rv
                    total += w
                    used += 1
            return total if used == n - 1 else float("inf")

        base = mst_weight()
        critical, pseudo = [], []
        for i in range(len(edges)):
            if mst_weight(skip=i) > base:
                critical.append(i)
            elif mst_weight(force=i) == base:
                pseudo.append(i)
        return [critical, pseudo]
