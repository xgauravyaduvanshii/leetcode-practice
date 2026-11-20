# 3289. The Two Sneaky Numbers of Digitville (Easy)
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
# Submission 2200001898 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # My thinking: count how often each number shows
        # up. The sneaky ones are the two that appear
        # exactly twice — everything else appears once.
        counts = Counter(nums)
        return [num for num, count in counts.items() if count == 2]
