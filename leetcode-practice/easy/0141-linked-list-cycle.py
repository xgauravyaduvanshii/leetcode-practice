# LeetCode 141. Linked List Cycle — Easy
# https://leetcode.com/problems/linked-list-cycle/
# Submission 2197444517 — Accepted, Python3
#
# My thinking: two pointers again — a slow one and a
# fast one that moves twice as fast. If there is a
# cycle, the fast one will eventually lap the slow
# one and they will meet. If the fast one reaches
# the end, there is no cycle.

class Solution:
    def hasCycle(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
