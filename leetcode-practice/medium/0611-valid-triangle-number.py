# LeetCode 611. Valid Triangle Number — Medium
# https://leetcode.com/problems/valid-triangle-number/
# Submission 2198879511 — Accepted, Python3
#
# My thinking: after sorting, I fix the longest
# side and slide two pointers across the smaller
# ones. When the two small sides are long enough,
# every side between them works too.

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for k in range(len(nums) - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    total += j - i
                    j -= 1
                else:
                    i += 1
        return total
