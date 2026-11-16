# LeetCode 1470. Shuffle the Array — Easy
# https://leetcode.com/problems/shuffle-the-array/
# Submission 2197581384 — Accepted, Python3
#
# My thinking: the first half of the array is the x
# values and the second half is the y values. I
# weave them together one by one — x1, y1, x2, y2 —
# and that is the shuffle.

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
