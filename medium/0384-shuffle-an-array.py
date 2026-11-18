# LeetCode 384. Shuffle an Array — Medium
# https://leetcode.com/problems/shuffle-an-array/
# Submission 2198766597 — Accepted, Python3
#
# My thinking: I keep the original array untouched
# and shuffle a fresh copy of it each time, so
# reset can always hand back the original order.

import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.original = list(nums)

    def reset(self) -> List[int]:
        return list(self.original)

    def shuffle(self) -> List[int]:
        shuffled = list(self.original)
        random.shuffle(shuffled)
        return shuffled
