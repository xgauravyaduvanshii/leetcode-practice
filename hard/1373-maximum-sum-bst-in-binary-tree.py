from __future__ import annotations


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # My thinking: a subtree is a search tree when its left
        # side stays below and its right side above — so each
        # subtree reports whether it qualifies, its range and
        # its sum, and the best sum seen anywhere wins.
        self.best = 0

        def dfs(node):
            if node is None:
                return (True, float("inf"), float("-inf"), 0)
            left_bst, left_min, left_max, left_sum = dfs(node.left)
            right_bst, right_min, right_max, right_sum = dfs(node.right)
            if left_bst and right_bst and left_max < node.val < right_min:
                total = left_sum + right_sum + node.val
                self.best = max(self.best, total)
                return (True, min(left_min, node.val), max(right_max, node.val), total)
            return (False, 0, 0, 0)

        dfs(root)
        return self.best
