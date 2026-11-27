# LeetCode 430. Flatten a Multilevel Doubly Linked List — Medium
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Submission 2198792409 — Accepted, Python3
#
# My thinking: I walk the list with a stack, always
# taking the child before the next node — that is
# depth-first order. Each node I visit gets linked
# after the previous one, and its child pointer is
# cleared as I go.

class Solution:
    def flatten(self, head):
        if not head:
            return None
        stack = [head]
        previous = None
        while stack:
            node = stack.pop()
            if previous:
                previous.next = node
                node.prev = previous
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
            previous = node
        head.prev = None
        return head
