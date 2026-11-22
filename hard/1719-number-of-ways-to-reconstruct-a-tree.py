# LeetCode 1719. Number Of Ways To Reconstruct A Tree — Hard
# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/
# Submission 2201110898 — Accepted, Python3
#
# My thinking: a subtree's root must touch every node
# in it, so I peel such a root off, split what is left
# into its connected parts, and repeat — if some part
# has no such root, no tree fits; if any part ever has
# two of them, the top of that part can flip, so there
# are two trees.

from collections import defaultdict

class Solution:
    def checkWays(self, pairs: list[list[int]]) -> int:
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
        nodes = set(adj)
        def rec(S):
            # True if this part is ambiguous, None if no tree fits it.
            if len(S) == 1:
                return False
            cands = [x for x in S if len(adj[x] & S) == len(S) - 1]
            if not cands:
                return None
            ambiguous = len(cands) > 1
            r = cands[0]
            rest = S - {r}
            seen = set()
            for start in rest:
                if start in seen:
                    continue
                stack = [start]
                comp = set()
                seen.add(start)
                while stack:
                    u = stack.pop()
                    comp.add(u)
                    for v in adj[u] & rest:
                        if v not in seen:
                            seen.add(v)
                            stack.append(v)
                sub = rec(comp)
                if sub is None:
                    return None
                ambiguous = ambiguous or sub
            return ambiguous
        result = rec(nodes)
        if result is None:
            return 0
        return 2 if result else 1
