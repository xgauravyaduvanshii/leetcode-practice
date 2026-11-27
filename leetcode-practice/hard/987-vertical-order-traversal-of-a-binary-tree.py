from __future__ import annotations

from collections import defaultdict, deque


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        # My thinking: walk the tree level by level, tagging each
        # node with its column and row, then read the columns off
        # in order, sorting ties by row then value.
        columns = defaultdict(list)
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, col = queue.popleft()
            columns[col].append((row, node.val))
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        return [
            [val for _, val in sorted(columns[col])]
            for col in sorted(columns)
        ]
