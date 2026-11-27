from __future__ import annotations


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # My thinking: a camera covers its parent and children, so
        # place cameras greedily from the leaves up — a leaf's
        # parent is the cheapest place to watch it.
        def dfs(node):
            if not node:
                return 2, 0
            left_state, left_cams = dfs(node.left)
            right_state, right_cams = dfs(node.right)
            cams = left_cams + right_cams
            if left_state == 0 or right_state == 0:
                return 1, cams + 1
            if left_state == 1 or right_state == 1:
                return 2, cams
            return 0, cams

        state, cams = dfs(root)
        return cams + (1 if state == 0 else 0)
