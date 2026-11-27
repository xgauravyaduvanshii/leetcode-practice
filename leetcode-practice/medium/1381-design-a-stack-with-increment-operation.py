# LeetCode 1381. Design a Stack With Increment Operation — Medium
# https://leetcode.com/problems/design-a-stack-with-increment-operation/
# Submission 2199044057 — Accepted, Python3
#
# My thinking: it is a plain stack with a size
# cap — pushes past the cap are ignored, pops
# on an empty stack return minus one — and
# increment adds to the first k entries.

from typing import List


class CustomStack:
    def __init__(self, maxSize: int):
        self.limit = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.limit:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
