# 3190. Find Minimum Operations to Make All Elements Divisible by Three (Easy)
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
# Submission 2199984449 — Accepted, Python3
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # My thinking: each number is either already
        # divisible by three, or one step away — either
        # up one or down one does it. So I add one for
        # every number that is not divisible yet.
        return sum(1 for num in nums if num % 3 != 0)
