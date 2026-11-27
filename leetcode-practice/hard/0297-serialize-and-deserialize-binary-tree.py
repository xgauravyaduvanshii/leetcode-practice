# LeetCode 297. Serialize and Deserialize Binary Tree — Hard
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Submission 2198401634 — Accepted, Python3
#
# My thinking: I write the tree down in preorder,
# one value at a time, marking every missing child
# with a #. That list is enough to rebuild the tree
# exactly, because the same preorder walk reads the
# values back in the same order — a # means stop
# here, anything else starts a new node whose
# children come next.

class Codec:
    def serialize(self, root) -> str:
        parts = []

        def dfs(node) -> None:
            if not node:
                parts.append("#")
                return
            parts.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(parts)

    def deserialize(self, data: str):
        values = iter(data.split(","))

        def build():
            val = next(values)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
