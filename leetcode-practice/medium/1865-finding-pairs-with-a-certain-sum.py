# 1865. Finding Pairs With a Certain Sum (Medium)
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
# Submission 2199951717 — Accepted, Python3
from collections import Counter
from typing import List


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        # My thinking: nums1 never changes, so the only
        # thing we need to keep fresh is how often each
        # value appears in nums2. A counter makes both
        # add and count cheap.
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        self.freq[old] -= 1
        self.nums2[index] = old + val
        self.freq[old + val] += 1

    def count(self, tot: int) -> int:
        pairs = 0
        for value in self.nums1:
            pairs += self.freq[tot - value]
        return pairs
