# LeetCode 993. Cousins in Binary Tree — Easy
# https://leetcode.com/problems/cousins-in-binary-tree/
# Submission 2197549347 — Accepted, Python3
#
# My thinking: two nodes are cousins if they sit at
# the same depth but have different parents. So I
# walk the whole tree and note down each target's
# depth and parent — then compare the two.

class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        info = {}

        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                info[node.val] = (depth, parent)
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)
        return info[x][0] == info[y][0] and info[x][1] != info[y][1]
