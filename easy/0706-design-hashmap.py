# LeetCode 706. Design HashMap — Easy
# https://leetcode.com/problems/design-hashmap/
# Submission 2197519594 — Accepted, Python3
#
# My thinking: same trick as the HashSet — the keys
# are only 0 to 1,000,000, so a plain list works as
# the map. Each slot holds the value for that key,
# or -1 when there is none. No built-in dict needed.

class MyHashMap:
    def __init__(self):
        self.data = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1
