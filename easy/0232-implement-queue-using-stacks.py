# LeetCode 232. Implement Queue using Stacks — Easy
# https://leetcode.com/problems/implement-queue-using-stacks/
# Submission 2197455368 — Accepted, Python3
#
# My thinking: two stacks. New items go on the first
# stack. When I need to take something out (or peek),
# I pour the first stack into the second one — that
# flips the order, so the oldest item ends up on top,
# exactly like a queue. I only pour when the second
# stack is empty, so each item moves at most twice.

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
