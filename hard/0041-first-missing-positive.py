# LeetCode 41. First Missing Positive — Hard
# https://leetcode.com/problems/first-missing-positive/
# Submission 2198365421 — Accepted, Python3
#
# My thinking: the answer has to be between 1 and
# n + 1, so I put every number where it belongs —
# value v goes to position v - 1 — by swapping
# numbers into place. Numbers outside that range
# are ignored. Then I scan from the start: the
# first position whose number does not match its
# position + 1 is the missing one.

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
