# LeetCode 173. Binary Search Tree Iterator — Medium
# https://leetcode.com/problems/binary-search-tree-iterator/
# Submission 2198437792 — Accepted, Python3
#
# My thinking: an inorder walk visits a BST in
# sorted order, so I keep a stack of the nodes
# still to come, starting with the leftmost path
# from the root. Each next() pops the smallest
# waiting node and pushes the leftmost path of its
# right child, so the stack always holds exactly
# the nodes that come next.

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)
