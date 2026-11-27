# LeetCode 347. Top K Frequent Elements — Medium
# https://leetcode.com/problems/top-k-frequent-elements/
# Submission 2198755921 — Accepted, Python3
#
# My thinking: I count how often each number
# appears, then take the k numbers with the biggest
# counts.

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [num for num, _ in counts.most_common(k)]
