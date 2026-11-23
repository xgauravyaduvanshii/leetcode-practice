# LeetCode 2458. Height of Binary Tree After Subtree Removal Queries — Hard
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
# Submission 2201753609 — Accepted, Python3
#
# My thinking: removing a subtree leaves
# the rest of the tree standing, and its
# height is either what survives above
# the cut or the tallest sibling branch
# left behind — I walk down once, carrying
# that best surviving height to each child.

import sys
sys.setrecursionlimit(300000)


class Solution:
    def treeQueries(self, root, queries: list[int]) -> list[int]:
        depth = {}
        height = {}
        ans = {}

        def dfs(u, d):
            depth[u.val] = d
            h = 0
            for child in (u.left, u.right):
                if child is not None:
                    h = max(h, 1 + dfs(child, d + 1))
            height[u.val] = h
            return h

        dfs(root, 0)

        def solve(u, up):
            ans[u.val] = up
            kids = [c for c in (u.left, u.right) if c is not None]
            for child in kids:
                best_sib = -1
                for sib in kids:
                    if sib is not child:
                        best_sib = max(best_sib, height[sib.val])
                solve(child, max(up, depth[u.val] + 1 + best_sib))

        solve(root, -1)
        return [ans[q] for q in queries]
