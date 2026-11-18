# LeetCode 284. Peeking Iterator — Medium
# https://leetcode.com/problems/peeking-iterator/
# Submission 2198733043 — Accepted, Python3
#
# My thinking: the iterator only moves forward, so
# I keep one element buffered ahead. Peek reads the
# buffer, next returns it and pulls the following
# element in, and hasNext just checks whether the
# buffer is empty.

class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._next = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self._next

    def next(self):
        current = self._next
        self._next = self._iterator.next() if self._iterator.hasNext() else None
        return current

    def hasNext(self):
        return self._next is not None
