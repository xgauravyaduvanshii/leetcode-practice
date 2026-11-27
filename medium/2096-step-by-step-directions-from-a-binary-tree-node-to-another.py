# LeetCode 2096. Step-By-Step Directions From a Binary Tree Node to Another — Medium
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# Submission 2204404363 — Accepted, Python3
#
# My thinking: I record every node's parent and the step (L or R) that
# reaches it from its parent, which gives me the root path of any
# node. The start and destination paths share a common prefix up to
# their lowest common ancestor, so the answer is 'U' for each extra
# step on the start side past that prefix, followed by the remaining
# L/R steps on the destination side.
class Solution:
    def getDirections(self, root: 'TreeNode | None', startValue: int, destValue: int) -> str:
        parent = {root.val: (None, '')}
        stack = [root]
        while stack:
            node = stack.pop()
            for child, d in ((node.left, 'L'), (node.right, 'R')):
                if child is not None and child.val not in parent:
                    parent[child.val] = (node.val, d)
                    stack.append(child)
            if startValue in parent and destValue in parent and len(parent) > 2:
                # cannot stop early in general; continue until both found
                pass
        def path_to(v):
            p = []
            while parent[v][0] is not None:
                p.append(parent[v][1])
                v = parent[v][0]
            return ''.join(reversed(p))
        ps = path_to(startValue)
        pd = path_to(destValue)
        i = 0
        while i < len(ps) and i < len(pd) and ps[i] == pd[i]:
            i += 1
        return 'U' * (len(ps) - i) + pd[i:]
