# LeetCode 1670. Design Front Middle Back Queue — Medium
# https://leetcode.com/problems/design-front-middle-back-queue/
# Submission 2199906835 — Accepted, Python3
#
# My thinking: I keep the queue as two halves
# — the front half in one deque, the back half
# in another. The middle is always the end of
# the front half, so every operation touches
# an end, and a rebalance keeps the halves
# even.

from collections import deque


class FrontMiddleBackQueue:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _rebalance(self):
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left):
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)
        self._rebalance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self._rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        val = self.left.pop()
        self._rebalance()
        return val

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._rebalance()
        return val
