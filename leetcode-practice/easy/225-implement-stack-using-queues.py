# 225. Implement Stack using Queues (Easy)
# https://leetcode.com/problems/implement-stack-using-queues/
# Submission 2199957132 — Accepted, Python3
from collections import deque


class MyStack:
    def __init__(self):
        # My thinking: a queue gives out the oldest item
        # first, but a stack needs the newest. So before
        # taking anything out, I move every older item to
        # the back of the queue — the newest one ends up
        # in front, ready to pop.
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        value = self.queue.popleft()
        self.queue.append(value)
        return value

    def empty(self) -> bool:
        return not self.queue
