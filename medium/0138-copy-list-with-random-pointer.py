# LeetCode 138. Copy List with Random Pointer — Medium
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Submission 2200866717 — Accepted, Python3
#
# My thinking: I walk the list once and copy every node,
# remembering each original node and its copy in a map;
# then I walk it again and wire each copy's next and
# random pointers through the map.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        node = head
        while node:
            old_to_new[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            copy = old_to_new[node]
            copy.next = old_to_new.get(node.next)
            copy.random = old_to_new.get(node.random)
            node = node.next
        return old_to_new[head]
