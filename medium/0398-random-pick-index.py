# LeetCode 398. Random Pick Index — Medium
# https://leetcode.com/problems/random-pick-index/
# Submission 2198776276 — Accepted, Python3
#
# My thinking: I record every position of each value
# once, up front. Picking is then just choosing one
# of the stored positions at random — every index
# holding the target is equally likely.

import random
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.positions = defaultdict(list)
        for index, num in enumerate(nums):
            self.positions[num].append(index)

    def pick(self, target: int) -> int:
        return random.choice(self.positions[target])
