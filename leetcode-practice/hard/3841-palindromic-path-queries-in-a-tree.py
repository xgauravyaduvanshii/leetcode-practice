# LeetCode 3841. Palindromic Path Queries in a Tree — Hard
# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
# Submission 2203285301 — Accepted, Python3


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # My thinking: a string can be rearranged into a
        # palindrome exactly when at most one character occurs
        # an odd number of times, so a path is captured by the
        # 26-bit mask of which letters appear oddly often on
        # it. Root the tree and keep pref[x], the xor of the
        # letter bits from the root down to x: the mask of the
        # u-v path is pref[u] ^ pref[v] ^ bit(s[lca]), since
        # the lowest common ancestor is counted twice by the
        # two root masks and must be counted once. An update
        # at node u flips the bit of every root path through
        # u, which is exactly the subtree of u in Euler tour
        # order, so a Fenwick tree does range-xor-update and
        # point-query in log n, and binary lifting gives the
        # lowest common ancestor in log n.
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG = 16
        up = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        parent = [-1] * n
        parent[0] = 0
        up[0][0] = 0
        timer = 0
        stack = [(0, iter(adj[0]))]
        tin[0] = timer
        timer += 1
        while stack:
            u, it = stack[-1]
            advanced = False
            for v in it:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                up[0][v] = u
                tin[v] = timer
                timer += 1
                stack.append((v, iter(adj[v])))
                advanced = True
                break
            if not advanced:
                tout[u] = timer - 1
                stack.pop()
        for j in range(1, LOG):
            for v in range(n):
                up[j][v] = up[j - 1][up[j - 1][v]]

        size = n + 2
        bit = [0] * size

        def bit_add(i, val):
            i += 1
            while i < size:
                bit[i] ^= val
                i += i & -i

        def bit_pref(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def range_add(l, r, val):
            bit_add(l, val)
            bit_add(r + 1, val)

        cur = [1 << (ord(c) - 97) for c in s]
        for v in range(n):
            range_add(tin[v], tout[v], cur[v])

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            d = depth[a] - depth[b]
            j = 0
            while d:
                if d & 1:
                    a = up[j][a]
                d >>= 1
                j += 1
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return up[0][a]

        ans = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u = int(p[1])
                new = 1 << (ord(p[2]) - 97)
                if cur[u] != new:
                    d = cur[u] ^ new
                    cur[u] = new
                    range_add(tin[u], tout[u], d)
            else:
                u = int(p[1])
                v = int(p[2])
                w = lca(u, v)
                mask = bit_pref(tin[u]) ^ bit_pref(tin[v]) ^ cur[w]
                ans.append(mask & (mask - 1) == 0)
        return ans
