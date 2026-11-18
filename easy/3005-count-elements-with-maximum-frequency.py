# LeetCode 3005. Count Elements With Maximum Frequency — Easy
# https://leetcode.com/problems/count-elements-with-maximum-frequency/
# Submission 2198714567 — Accepted, Python3
#
# My thinking: I count how often each number appears,
# find the highest frequency, and add up the counts
# of every number that reaches it.

from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        highest = max(counts.values())
        return sum(count for count in counts.values() if count == highest)
