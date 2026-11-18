# LeetCode 652. Find Duplicate Subtrees — Medium
# https://leetcode.com/problems/find-duplicate-subtrees/
# Submission 2198899002 — Accepted, Python3
#
# My thinking: a subtree is fully described by its
# value and the descriptions of its children. I
# serialise every subtree that way and collect the
# ones whose description shows up more than once.

from __future__ import annotations

from collections import defaultdict
from typing import List, Optional


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        serials = defaultdict(list)

        def serialize(node):
            if not node:
                return "#"
            key = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            serials[key].append(node)
            return key

        serialize(root)
        return [nodes[0] for nodes in serials.values() if len(nodes) > 1]
