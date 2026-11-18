# LeetCode 460. LFU Cache — Hard
# https://leetcode.com/problems/lfu-cache/
# Submission 2198658893 — Accepted, Python3
#
# My thinking: I keep one ordered dict per frequency,
# so the least frequently used key is always the first
# entry of the lowest frequency bucket, and keys with
# the same frequency stay in least-recently-used order.
# Every get or put bumps the key into the next bucket.

from collections import OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        self.frequencies = {}
        self.by_frequency = {}
        self.lowest_frequency = 0

    def _touch(self, key):
        freq = self.frequencies[key]
        del self.by_frequency[freq][key]
        if not self.by_frequency[freq] and freq == self.lowest_frequency:
            self.lowest_frequency += 1
        self.frequencies[key] = freq + 1
        self.by_frequency.setdefault(freq + 1, OrderedDict())[key] = None

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self._touch(key)
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.values:
            self.values[key] = value
            self._touch(key)
            return
        if len(self.values) == self.capacity:
            evict, _ = self.by_frequency[self.lowest_frequency].popitem(last=False)
            del self.values[evict]
            del self.frequencies[evict]
        self.values[key] = value
        self.frequencies[key] = 1
        self.by_frequency.setdefault(1, OrderedDict())[key] = None
        self.lowest_frequency = 1
