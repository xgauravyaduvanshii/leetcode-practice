# LeetCode 1146. Snapshot Array — Medium
# https://leetcode.com/problems/snapshot-array/
# Submission 2199005502 — Accepted, Python3
#
# My thinking: each index keeps a small history
# of its values with the snapshot number they
# were set at. A lookup finds the newest entry
# that is no later than the snapshot asked for.

import bisect
from typing import List


class SnapshotArray:
    def __init__(self, length: int):
        self.history = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1] = (self.snap_id, val)
        else:
            self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        entries = self.history[index]
        pos = bisect.bisect_right(entries, (snap_id, float("inf"))) - 1
        return entries[pos][1]
