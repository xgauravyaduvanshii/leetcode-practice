# LeetCode 2612. Minimum Reverse Operations — Hard
# https://leetcode.com/problems/minimum-reverse-operations/
# Submission 2201849724 — Accepted, Python3
#
# My thinking: reversing a window of
# length k throws the single 1 to a
# mirror spot, and every mirror spot in
# reach shares one parity — so I keep
# the untouched spots of each parity in
# a chain that always points at the next
# one, and sweep them up the moment a
# window can reach them.

from collections import deque


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: list[int], k: int) -> list[int]:
        ans = [-1] * n
        ans[p] = 0
        banned_set = set(banned)
        # DSU "next unvisited" chains, one per parity, over the index y // 2.
        # find(x) returns the smallest unvisited index >= x (in y//2 space).
        size = (n + 1) // 2 + 1
        parent = [list(range(size)), list(range(size))]

        def find(par, x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        def remove(par, y):
            i = y // 2
            par[i] = find(par, i + 1)

        for b in banned_set:
            remove(parent[b & 1], b)
        remove(parent[p & 1], p)
        q = deque([p])
        while q:
            x = q.popleft()
            l_min = max(0, x - k + 1)
            l_max = min(x, n - k)
            y_min = 2 * l_min + k - 1 - x
            y_max = 2 * l_max + k - 1 - x
            par = parent[(k - 1 - x) & 1]
            # first index with the right parity that is >= y_min
            start = y_min if (y_min & 1) == ((k - 1 - x) & 1) else y_min + 1
            i = find(par, start // 2)
            while True:
                y = 2 * i + ((k - 1 - x) & 1)
                if y > y_max or i >= size - 1:
                    break
                ans[y] = ans[x] + 1
                q.append(y)
                remove(par, y)
                i = find(par, i)
        return ans
