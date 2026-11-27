# LeetCode 3715. Sum of Perfect Square Ancestors — Hard
# https://leetcode.com/problems/sum-of-perfect-square-ancestors/
# Submission 2203059655 — Accepted, Python3
from typing import List


class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        # My thinking: nums[i] * nums[a] is a perfect square
        # exactly when the two numbers have the same squarefree
        # part — the product of the primes that occur to an odd
        # power in each number, since the even-power primes
        # already form a square on their own. So I replace every
        # value by its squarefree part, then walk the tree from
        # the root keeping a count of the squarefree parts seen
        # on the current root path: every ancestor whose part
        # matches the current node's part forms a perfect square
        # with it. The count is added when I enter a node and
        # removed when I leave it, so it always holds just the
        # ancestors, never the siblings or the node itself.
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Smallest prime factor sieve up to the largest value.
        limit = max(nums)
        spf = list(range(limit + 1))
        for i in range(2, int(limit ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def squarefree(x: int) -> int:
            # My thinking: strip the primes in pairs — only a
            # prime left over an odd number of times survives.
            res = 1
            while x > 1:
                p = spf[x]
                odd = 0
                while x % p == 0:
                    x //= p
                    odd ^= 1
                if odd:
                    res *= p
            return res

        part = [squarefree(x) for x in nums]
        on_path = {}
        ans = 0
        # Iterative DFS with an explicit exit marker, so a
        # 1e5-deep chain never hits the recursion limit.
        stack = [(0, -1, False)]
        while stack:
            node, parent, exiting = stack.pop()
            if exiting:
                p = part[node]
                on_path[p] -= 1
                if on_path[p] == 0:
                    del on_path[p]
                continue
            ans += on_path.get(part[node], 0)
            on_path[part[node]] = on_path.get(part[node], 0) + 1
            stack.append((node, parent, True))
            for nb in adj[node]:
                if nb != parent:
                    stack.append((nb, node, False))
        return ans
