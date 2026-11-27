# 3046. Split the Array (Easy)
# https://leetcode.com/problems/split-the-array/
# Submission 2199972861 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # My thinking: the two halves must each hold
        # distinct numbers, so no number may appear more
        # than twice — one copy per half. If every count
        # is at most two, the split works.
        counts = Counter(nums)
        return all(count <= 2 for count in counts.values())
