# LeetCode 1656. Design an Ordered Stream — Easy
# https://leetcode.com/problems/design-an-ordered-stream/
# Submission 2197592198 — Accepted, Python3
#
# My thinking: I store each value at its id and keep
# a pointer at the next id I am waiting for. After
# every insert, I hand out the longest run of
# consecutive values starting at that pointer,
# moving the pointer forward as I go.

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value
        result = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        return result
