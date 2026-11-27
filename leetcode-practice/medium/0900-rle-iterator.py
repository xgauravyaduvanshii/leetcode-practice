# LeetCode 900. RLE Iterator — Medium
# https://leetcode.com/problems/rle-iterator/
# Submission 2198965705 — Accepted, Python3
#
# My thinking: I walk through the encoded pairs
# one at a time, eating into the current run
# until the request is covered. If I run out of
# pairs, there is nothing left to return.

from typing import List


class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding):
            count = self.encoding[self.index]
            value = self.encoding[self.index + 1]
            if n <= count:
                self.encoding[self.index] -= n
                return value
            n -= count
            self.index += 2
        return -1
