# LeetCode 155. Min Stack — Medium
# https://leetcode.com/problems/min-stack/
# Submission 2197447202 — Accepted, Python3
#
# My thinking: I keep two stacks. The main one holds
# everything, and a second one only holds the minimums
# so far. When I push a value that is smaller than (or
# equal to) the current minimum, it goes on the second
# stack too. When I pop, if I pop the current minimum,
# I pop it from the second stack as well — so getMin
# is always just the top of that second stack.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
