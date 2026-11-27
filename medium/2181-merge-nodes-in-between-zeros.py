# LeetCode 2181. Merge Nodes in Between Zeros — Medium
# https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Submission 2204489212 — Accepted, Python3
#
# My thinking: the list starts and ends with zero, and the nodes between
# two zeros belong to one merged node. I walk the list once, adding up
# values until I hit a zero, then emit a new node with that sum and
# reset the running total.
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        tail = dummy
        cur = head.next
        s = 0
        while cur:
            if cur.val == 0:
                tail.next = ListNode(s)
                tail = tail.next
                s = 0
            else:
                s += cur.val
            cur = cur.next
        return dummy.next
