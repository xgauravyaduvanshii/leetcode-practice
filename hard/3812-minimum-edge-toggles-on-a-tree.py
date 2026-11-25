# LeetCode 3812. Minimum Edge Toggles on a Tree — Hard
# https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/
# Submission 2203190345 — Accepted, Python3
from typing import List


class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        # My thinking: toggling an edge flips both of its ends,
        # so a node ends up flipped exactly when an odd number
        # of its incident edges are toggled. On a tree the
        # choice is forced from the leaves up: a leaf that
        # still mismatches its target can only be fixed by
        # toggling the edge to its parent, and that toggle
        # flips the parent's remaining need as well. So I
        # root the tree at 0 and walk it in postorder; each
        # node reports whether the edge to its parent must be
        # toggled, which is its own mismatch xored with the
        # toggles already chosen on the edges to its children.
        # The root has no parent edge, so if it still needs a
        # flip the transformation is impossible. The forced
        # choices are the unique minimum-length solution, and
        # sorting the chosen indices gives the required order.
        # I use an explicit stack because a chain of 10^5
        # nodes would overflow Python's recursion limit.
        g = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            g[a].append((b, i))
            g[b].append((a, i))
        ans = []
        need = [False] * n
        stack = [(0, -1, 0)]
        while stack:
            a, fa, state = stack.pop()
            if state == 0:
                stack.append((a, fa, 1))
                for b, _ in g[a]:
                    if b != fa:
                        stack.append((b, a, 0))
            else:
                rev = start[a] != target[a]
                for b, i in g[a]:
                    if b != fa and need[b]:
                        ans.append(i)
                        rev = not rev
                need[a] = rev
        if need[0]:
            return [-1]
        ans.sort()
        return ans
