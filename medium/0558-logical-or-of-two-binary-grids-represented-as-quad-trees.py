# LeetCode 558. Logical OR of Two Binary Grids Represented as Quad-Trees — Medium
# https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/
# Submission 2198863994 — Accepted, Python3
#
# My thinking: a leaf decides its whole square — a
# true leaf wins the OR, a false leaf defers to the
# other tree. Otherwise I combine the four quarters
# and fold them back into one leaf when they all
# agree.

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        children = [topLeft, topRight, bottomLeft, bottomRight]
        if all(child.isLeaf for child in children) and len({child.val for child in children}) == 1:
            return Node(children[0].val, True)
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
