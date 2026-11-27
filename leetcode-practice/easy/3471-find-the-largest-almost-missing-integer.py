# 3471. Find the Largest Almost Missing Integer (Easy)
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/
# Submission 2200020195 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # My thinking: an integer is almost missing
        # when it shows up in exactly one window of
        # size k. I count, for each value, how many
        # windows hold it, and take the largest value
        # whose count is exactly one.
        windows = Counter()
        for start in range(len(nums) - k + 1):
            for value in set(nums[start:start + k]):
                windows[value] += 1
        best = -1
        for value, count in windows.items():
            if count == 1:
                best = max(best, value)
        return best
