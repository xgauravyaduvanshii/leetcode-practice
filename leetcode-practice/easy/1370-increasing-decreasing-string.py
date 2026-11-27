# LeetCode 1370. Increasing Decreasing String — Easy
# https://leetcode.com/problems/increasing-decreasing-string/
# Submission 2197574157 — Accepted, Python3
#
# My thinking: I count the letters, then keep taking
# them in a cycle — smallest to largest, then
# largest back to smallest, one of each letter that
# is still left — until none remain.

from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        counts = Counter(s)
        result = []
        while counts:
            for ch in sorted(counts):
                result.append(ch)
                counts[ch] -= 1
                if counts[ch] == 0:
                    del counts[ch]
            for ch in sorted(counts, reverse=True):
                result.append(ch)
                counts[ch] -= 1
                if counts[ch] == 0:
                    del counts[ch]
        return "".join(result)
