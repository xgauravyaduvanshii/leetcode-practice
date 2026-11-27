# LeetCode 519. Random Flip Matrix — Medium
# https://leetcode.com/problems/random-flip-matrix/
# Submission 2198839160 — Accepted, Python3
#
# My thinking: I keep a virtual list of the cells
# still unflipped. Picking one at random and
# swapping it with the last unflipped cell shrinks
# the list — no need to store the whole matrix.
# Reset just restores the full list.

import random
from typing import List


class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.swapped = {}

    def flip(self) -> List[int]:
        index = random.randint(0, self.total - 1)
        self.total -= 1
        value = self.swapped.get(index, index)
        self.swapped[index] = self.swapped.get(self.total, self.total)
        return [value // self.n, value % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.swapped = {}
