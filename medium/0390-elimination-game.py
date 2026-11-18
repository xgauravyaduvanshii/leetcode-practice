# LeetCode 390. Elimination Game — Medium
# https://leetcode.com/problems/elimination-game/
# Submission 2198772281 — Accepted, Python3
#
# My thinking: I track the first surviving number,
# the gap between survivors, and how many are left.
# Each pass doubles the gap and halves the count;
# the head moves when I sweep left to right, or when
# an odd count leaves the head exposed on the way
# back.

class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left = True
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
        return head
