# LeetCode 2385. Amount of Time for Binary Tree to Be Infected — Medium
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
# Submission 2204778327 — Accepted, Python3
#
# My thinking: first map every node to its parent with a stack walk
# (also finding the start node), then BFS from the start node over
# left/right/parent neighbours. The distance of the last node reached
# is the number of minutes until the whole tree is infected.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        parent = {}
        start_node = None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == start:
                start_node = node
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        from collections import deque
        seen = {start_node}
        q = deque([(start_node, 0)])
        ans = 0
        while q:
            node, d = q.popleft()
            ans = d
            for nb in (node.left, node.right, parent.get(node)):
                if nb is not None and nb not in seen:
                    seen.add(nb)
                    q.append((nb, d + 1))
        return ans
