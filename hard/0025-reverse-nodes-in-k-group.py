# LeetCode 25. Reverse Nodes in k-Group — Hard
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Submission 2198363336 — Accepted, Python3
#
# My thinking: I handle the list one group of k
# nodes at a time. First I check that k nodes are
# actually there — if not, the tail stays as it is.
# Then I flip the arrows inside the group, link
# the flipped group back into the list, and move
# on to the next group.

class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            prev, current = group_next, group_prev.next
            while current != group_next:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
