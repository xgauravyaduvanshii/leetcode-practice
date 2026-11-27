# 3718. Smallest Missing Multiple of K (Easy)
# https://leetcode.com/problems/smallest-missing-multiple-of-k/
# Submission 2200055139 — Accepted, Python3
from typing import List


class Solution:
    def smallestMissingMultiple(self, nums: List[int], k: int) -> int:
        # My thinking: walk through the multiples of
        # k — k, 2k, 3k and so on — and take the first
        # one that is missing from the array.
        present = set(nums)
        x = k
        while x in present:
            x += k
        return x
