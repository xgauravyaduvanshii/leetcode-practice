# LeetCode 381. Insert Delete GetRandom O(1) - Duplicates allowed — Hard
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# Submission 2198408704 — Accepted, Python3
#
# My thinking: I keep all the values in a list and
# remember, for each value, the set of positions it
# sits at. To remove a value I take one of its
# positions and move the last value in the list
# into that spot, updating that value's positions
# — so insert, remove and a random pick are all
# constant time.

import random
from collections import defaultdict


class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.places = defaultdict(set)

    def insert(self, val: int) -> bool:
        new = val not in self.places
        self.places[val].add(len(self.values))
        self.values.append(val)
        return new

    def remove(self, val: int) -> bool:
        if val not in self.places or not self.places[val]:
            return False
        idx = self.places[val].pop()
        last = self.values[-1]
        self.values[idx] = last
        self.places[last].add(idx)
        self.places[last].discard(len(self.values) - 1)
        self.values.pop()
        if not self.places[val]:
            del self.places[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
