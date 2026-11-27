# LeetCode 2130. Maximum Twin Sum of a Linked List — Medium
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Submission 2200975139 — Accepted, Python3
#
# My thinking: I reverse the second half of the list,
# then walk both halves together and take the biggest
# sum of each mirrored pair.

class Solution:
    def pairSum(self, head) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        best = 0
        first, second = head, prev
        while second:
            best = max(best, first.val + second.val)
            first = first.next
            second = second.next
        return best
