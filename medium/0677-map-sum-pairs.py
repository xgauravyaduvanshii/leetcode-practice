# LeetCode 677. Map Sum Pairs — Medium
# https://leetcode.com/problems/map-sum-pairs/
# Submission 2198908864 — Accepted, Python3
#
# My thinking: a dictionary remembers the latest
# value for each key, and a prefix sum is just the
# total of every stored key that starts with that
# prefix.

class MapSum:
    def __init__(self):
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        self.values[key] = val

    def sum(self, prefix: str) -> int:
        return sum(val for key, val in self.values.items() if key.startswith(prefix))
