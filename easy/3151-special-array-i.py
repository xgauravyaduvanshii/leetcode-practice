# 3151. Special Array I (Easy)
# https://leetcode.com/problems/special-array-i/
# Submission 2199980027 — Accepted, Python3
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # My thinking: a special array alternates even
        # and odd. I walk along and check each neighbour
        # pair — two neighbours with the same parity
        # break the pattern.
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
