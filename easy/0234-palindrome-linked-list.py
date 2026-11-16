# LeetCode 234. Palindrome Linked List — Easy
# https://leetcode.com/problems/palindrome-linked-list/
# Submission 2197455968 — Accepted, Python3
#
# My thinking: I find the middle with a slow and a
# fast pointer, then reverse the second half of the
# list in place. After that the two halves are easy
# to compare — I walk them together from the start
# and from the middle, checking that every pair
# matches.

class Solution:
    def isPalindrome(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        previous = None
        while slow:
            next_node = slow.next
            slow.next = previous
            previous = slow
            slow = next_node
        left, right = head, previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
