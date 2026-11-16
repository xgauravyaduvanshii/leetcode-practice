# LeetCode 160. Intersection of Two Linked Lists — Easy
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Submission 2197447768 — Accepted, Python3
#
# My thinking: I walk both lists at the same time. When
# a pointer reaches the end of its list, I jump it to
# the start of the other list. That way both pointers
# travel the same total distance, so if the lists meet,
# they meet at the intersection — and if they never
# meet, both end up at None together.

class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
