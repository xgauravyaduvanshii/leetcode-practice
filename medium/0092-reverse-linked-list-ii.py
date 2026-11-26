# LeetCode 92. Reverse Linked List II — Medium
# https://leetcode.com/problems/reverse-linked-list-ii/
# Submission 2203973170 — Accepted, Python3
#
# My thinking:
# Only the segment from position left to position right needs reversing;
# everything before left and after right stays exactly as it is.
# I put a dummy node in front of the head so the case left == 1 needs
# no special handling. Then I walk to the node just before the segment
# (call it prev) and take the first node of the segment as its tail.
# From there I reverse the segment one link at a time: at each step I
# lift the node after the tail out and plug it in right after prev,
# so the segment grows reversed at the front while the tail stays put.
# After right - left such moves the segment is fully reversed, and I
# reconnect its tail to the untouched remainder of the list.

from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional["ListNode"], left: int, right: int) -> Optional["ListNode"]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # tail is the first node of the segment; it ends up last after reversal.
        tail = prev.next
        for _ in range(right - left):
            nxt = tail.next
            tail.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next


if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def build(values):
        dummy = ListNode(0)
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def to_list(head):
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out

    s = Solution()
    # Sample 1: [1,2,3,4,5], left = 2, right = 4 -> [1,4,3,2,5].
    assert to_list(s.reverseBetween(build([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    # Sample 2: [5], left = 1, right = 1 -> [5].
    assert to_list(s.reverseBetween(build([5]), 1, 1)) == [5]
    # Reverse the whole list.
    assert to_list(s.reverseBetween(build([1, 2, 3, 4, 5]), 1, 5)) == [5, 4, 3, 2, 1]
    # Reverse from the head, partial.
    assert to_list(s.reverseBetween(build([1, 2, 3]), 1, 2)) == [2, 1, 3]
    # Reverse at the tail only.
    assert to_list(s.reverseBetween(build([1, 2, 3, 4]), 3, 4)) == [1, 2, 4, 3]
    # Two-node list, full reversal.
    assert to_list(s.reverseBetween(build([1, 2]), 1, 2)) == [2, 1]
    print("All sample checks passed.")
