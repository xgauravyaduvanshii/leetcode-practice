# 3731. Find Missing Elements (Easy)
# https://leetcode.com/problems/find-missing-elements/
# Submission 2200056836 — Accepted, Python3
from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # My thinking: the smallest and largest
        # numbers are still there, so every whole
        # number between them should be there too.
        # I list the ones that are missing, in order.
        present = set(nums)
        return [x for x in range(min(nums), max(nums) + 1) if x not in present]
