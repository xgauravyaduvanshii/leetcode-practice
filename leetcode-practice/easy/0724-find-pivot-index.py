# LeetCode 724. Find Pivot Index — Easy
# https://leetcode.com/problems/find-pivot-index/
# Submission 2197522051 — Accepted, Python3
#
# My thinking: I add up everything once. Then I walk
# through the numbers keeping the sum of what is on
# the left. At each spot, the right side is the
# total minus the left side minus this number — if
# the two sides match, I have found the pivot.

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            left += num
        return -1
