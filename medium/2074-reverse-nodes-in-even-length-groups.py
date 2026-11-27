# LeetCode 2074. Reverse Nodes in Even Length Groups — Medium
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
# Submission 2204398080 — Accepted, Python3
#
# My thinking: I take the list in groups of size 1, 2, 3, ... and
# collect each group's nodes. When a group has even length I reverse
# its links in place and splice it back between the previous part and
# the next group; odd groups stay as they are. A dummy head keeps the
# splicing uniform.
class Solution:
    def reverseEvenLengthGroups(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        size = 1
        while cur:
            group = []
            node = cur
            for _ in range(size):
                if not node:
                    break
                group.append(node)
                node = node.next
            nxt = node
            if len(group) % 2 == 0:
                for i in range(len(group) - 1, 0, -1):
                    group[i].next = group[i - 1]
                group[0].next = nxt
                prev.next = group[-1]
                prev = group[0]
            else:
                prev = group[-1]
            cur = nxt
            size += 1
        return dummy.next
