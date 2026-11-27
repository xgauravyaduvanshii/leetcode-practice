# LeetCode 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points — Medium
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
# Submission 2204388897 — Accepted, Python3
#
# My thinking: a critical point is a node that is strictly greater
# than both neighbours or strictly smaller than both. I walk the list
# once, remembering the first and the most recent critical positions:
# the maximum distance is last minus first, the minimum distance is
# the smallest gap between consecutive critical points. With fewer
# than two critical points the answer is [-1, -1].
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        prev = head
        cur = head.next
        idx = 1
        first = -1
        last = -1
        mind = 10 ** 9
        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                if first == -1:
                    first = idx
                else:
                    mind = min(mind, idx - last)
                last = idx
            prev = cur
            cur = cur.next
            idx += 1
        if first == -1 or first == last:
            return [-1, -1]
        return [mind, last - first]
