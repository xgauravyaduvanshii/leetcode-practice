# LeetCode 2265. Count Nodes Equal to Average of Subtree — Medium
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
# Submission 2204520970 — Accepted, Python3
#
# My thinking: a node's subtree average needs its subtree sum and size,
# which a single depth-first pass returns bottom-up. At each node I add
# the children's sums and counts plus the node itself, and count the
# node when the floored average equals its value.
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return (0, 0)
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            s = ls + rs + node.val
            c = lc + rc + 1
            if s // c == node.val:
                self.ans += 1
            return (s, c)

        dfs(root)
        return self.ans
