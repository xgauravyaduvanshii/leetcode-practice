# LeetCode 257. Binary Tree Paths — Easy
# https://leetcode.com/problems/binary-tree-paths/
# Submission 2197457817 — Accepted, Python3
#
# My thinking: I walk down the tree, carrying the
# path so far as a string. At each node I add its
# value; when I reach a leaf, that whole path is one
# answer. Otherwise I add an arrow and keep going
# down both sides.

class Solution:
    def binaryTreePaths(self, root) -> list[str]:
        paths = []

        def dfs(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
                return
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return paths
