# LeetCode 449. Serialize and Deserialize BST — Medium
# https://leetcode.com/problems/serialize-and-deserialize-bst/
# Submission 2198803116 — Accepted, Python3
#
# My thinking: a BST's preorder walk is enough to
# rebuild it — each value goes into the first open
# slot its size allows. I write the values out in
# preorder, then rebuild them with a recursive
# builder bounded by the smallest and largest value
# each subtree may hold.

class Codec:
    def serialize(self, root):
        values = []

        def preorder(node):
            if not node:
                return
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(values)

    def deserialize(self, data):
        if not data:
            return None
        values = [int(v) for v in data.split()]
        index = [0]

        def build(lower, upper):
            if index[0] == len(values):
                return None
            value = values[index[0]]
            if value < lower or value > upper:
                return None
            index[0] += 1
            node = TreeNode(value)
            node.left = build(lower, value)
            node.right = build(value, upper)
            return node

        return build(float("-inf"), float("inf"))
