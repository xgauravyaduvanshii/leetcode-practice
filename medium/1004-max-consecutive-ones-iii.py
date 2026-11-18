# LeetCode 1004. Max Consecutive Ones III — Medium
# https://leetcode.com/problems/max-consecutive-ones-iii/
# Submission 2198983635 — Accepted, Python3
#
# My thinking: I grow a window and count the
# zeroes inside it. When there are more zeroes
# than I am allowed to flip, I shrink the window
# from the left until it fits again.

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        best = 0
        left = 0
        zeros = 0
        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
