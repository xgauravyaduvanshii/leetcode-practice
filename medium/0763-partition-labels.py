# LeetCode 763. Partition Labels — Medium
# https://leetcode.com/problems/partition-labels/
# Submission 2198930607 — Accepted, Python3
#
# My thinking: a partition can only end where the
# last occurrence of every letter inside it has
# passed. I track the farthest last occurrence
# seen so far and cut as soon as I reach it.

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        result = []
        start = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
