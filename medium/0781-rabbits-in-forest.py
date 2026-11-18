# LeetCode 781. Rabbits in Forest — Medium
# https://leetcode.com/problems/rabbits-in-forest/
# Submission 2198936055 — Accepted, Python3
#
# My thinking: a rabbit that says "n others like
# me" belongs to a group of n + 1. I count how
# many gave the same answer and round up to whole
# groups of that size.

from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        for answer, count in Counter(answers).items():
            group_size = answer + 1
            groups = (count + group_size - 1) // group_size
            total += groups * group_size
        return total
