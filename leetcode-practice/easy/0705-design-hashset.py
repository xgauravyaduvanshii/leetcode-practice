# LeetCode 705. Design HashSet — Easy
# https://leetcode.com/problems/design-hashset/
# Submission 2197519090 — Accepted, Python3
#
# My thinking: the keys are only 0 to 1,000,000, so
# I can use a plain boolean list as the set itself
# — index = key, True = present. No built-in set
# needed (LeetCode rejects set() here). Add sets
# the slot to True, remove sets it to False, and
# contains just reads it.

class MyHashSet:
    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]
