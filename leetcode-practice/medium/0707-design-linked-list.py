# LeetCode 707. Design Linked List — Medium
# https://leetcode.com/problems/design-linked-list/
# Submission 2197520993 — Accepted, Python3
#
# My thinking: I keep a dummy node in front of the
# real list, so adding or deleting at the head works
# the same as anywhere else. Every operation walks
# from the dummy to the node before the one I want,
# and I keep a size counter so I can reject indexes
# that are out of range.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.dummy.next
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = ListNode(val, prev.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1
