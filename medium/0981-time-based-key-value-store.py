# LeetCode 981. Time Based Key-Value Store — Medium
# https://leetcode.com/problems/time-based-key-value-store/
# Submission 2198980416 — Accepted, Python3
#
# My thinking: timestamps arrive in order, so I
# keep a list of times and a list of values per
# key. A query is a binary search for the latest
# time at or before the one asked for.

import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        times = self.times.get(key, [])
        index = bisect.bisect_right(times, timestamp) - 1
        return self.values[key][index] if index >= 0 else ""
