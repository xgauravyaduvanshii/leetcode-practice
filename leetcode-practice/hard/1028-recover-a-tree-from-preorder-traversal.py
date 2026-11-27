from __future__ import annotations


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # My thinking: the dashes tell the depth, so keep a stack
        # of the path down — each new node attaches as the left
        # child first, then the right.
        stack = []
        i = 0
        n = len(traversal)
        while i < n:
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1
            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            node = TreeNode(value)
            while len(stack) > depth:
                stack.pop()
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
        return stack[0]
