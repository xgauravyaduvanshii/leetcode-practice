# LeetCode 117. Populating Next Right Pointers in Each Node II — Medium
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Submission 2204011543 — Accepted, Python3
#
# My thinking: I walk the tree level by level, but instead of a queue
# I reuse the next pointers I am building. For each level I keep a
# dummy node whose next chain collects that level's children in order:
# I scan the current level through its next pointers, and every time
# I meet a left or right child I append it to the dummy chain. When
# the level is done, the dummy's next is the first node of the next
# level, so I move down and repeat. This links every node to its
# right neighbour using only constant extra space, and it works for
# any binary tree, not just a perfect one.

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            dummy = Node(0)
            tail = dummy
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = dummy.next
        return root
