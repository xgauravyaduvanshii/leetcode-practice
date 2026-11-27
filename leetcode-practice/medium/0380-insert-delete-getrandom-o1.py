# LeetCode 380. Insert Delete GetRandom O(1) — Medium
# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Submission 2198765574 — Accepted, Python3
#
# My thinking: a list gives random access and a
# dictionary gives instant lookup. To delete I swap
# the element with the last one, update the moved
# element's position, and pop the end — every
# operation stays constant time.

import random


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        self.positions[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        index = self.positions[val]
        last = self.values[-1]
        self.values[index] = last
        self.positions[last] = index
        self.values.pop()
        del self.positions[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
