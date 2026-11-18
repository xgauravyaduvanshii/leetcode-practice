# LeetCode 805. Split Array With Same Average — Hard
# https://leetcode.com/problems/split-array-with-same-average/
# Submission 2198676617 — Accepted, Python3
#
# My thinking: if a split works, some group of k
# numbers must add up to exactly total times k over
# n. So I build every achievable sum for every group
# size — one pass, adding each number to the sets
# above it — and then check whether any group size
# has the sum it would need.

from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        possible = [set() for _ in range(n + 1)]
        possible[0].add(0)
        for num in nums:
            for k in range(n - 1, -1, -1):
                for s in possible[k]:
                    possible[k + 1].add(s + num)
        for k in range(1, n):
            if (total * k) % n == 0 and (total * k) // n in possible[k]:
                return True
        return False
