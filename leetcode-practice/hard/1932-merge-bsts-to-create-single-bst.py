# LeetCode 1932. Merge BSTs to Create Single BST — Hard
# https://leetcode.com/problems/merge-bsts-to-create-single-bst/
# Submission 2201246087 — Accepted, Python3
#
# My thinking: the final root is the one tree whose
# root is no other tree's leaf — I graft each other
# tree onto the leaf that carries its root value,
# checking the binary-search bounds as I go, and
# the merge only counts when every tree is used.

from __future__ import annotations
from typing import Optional

class Solution:
    def canMerge(self, trees: list[TreeNode]) -> Optional[TreeNode]:
        roots = {}
        leaves = [set() for _ in trees]
        for i, t in enumerate(trees):
            roots[t.val] = t
            stack = [t]
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None:
                    leaves[i].add(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
        final = None
        for i, t in enumerate(trees):
            if all(t.val not in leaves[j] for j in range(len(trees)) if j != i):
                if final is not None:
                    return None
                final = t
        if final is None:
            return None
        merged = [0]

        def dfs(node, lo, hi):
            if node is None:
                return True
            if not (lo < node.val < hi):
                return False
            if node.left is None and node.right is None:
                sub = roots.get(node.val)
                if sub is not None and sub is not node:
                    merged[0] += 1
                    del roots[node.val]
                    node.left, node.right = sub.left, sub.right
                    return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
                return True
            return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)

        if not dfs(final, float("-inf"), float("inf")):
            return None
        if merged[0] != len(trees) - 1:
            return None
        return final
