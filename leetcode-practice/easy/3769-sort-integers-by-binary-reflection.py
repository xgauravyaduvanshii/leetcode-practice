# 3769. Sort Integers by Binary Reflection (Easy)
# https://leetcode.com/problems/sort-integers-by-binary-reflection/
# Submission 2200062519 — Accepted, Python3
from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        # My thinking: flip each number's binary digits
        # around to get its reflection, then sort by
        # that — and when two reflections tie, the
        # smaller number comes first.
        def reflect(x: int) -> int:
            return int(bin(x)[2:][::-1], 2)

        return sorted(nums, key=lambda x: (reflect(x), x))
