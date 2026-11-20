class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        # My thinking: shared roads help both, so lay those
        # first — then add each person's own roads only where
        # they still need a connection, and drop the rest.
        parent_a = list(range(n + 1))
        parent_b = list(range(n + 1))

        def find(parent, x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(parent, x, y):
            rx, ry = find(parent, x), find(parent, y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        used = 0
        for t, u, v in edges:
            if t == 3:
                a = union(parent_a, u, v)
                b = union(parent_b, u, v)
                if a or b:
                    used += 1
        for t, u, v in edges:
            if t == 1 and union(parent_a, u, v):
                used += 1
        for t, u, v in edges:
            if t == 2 and union(parent_b, u, v):
                used += 1
        comps_a = len({find(parent_a, i) for i in range(1, n + 1)})
        comps_b = len({find(parent_b, i) for i in range(1, n + 1)})
        if comps_a != 1 or comps_b != 1:
            return -1
        return len(edges) - used
