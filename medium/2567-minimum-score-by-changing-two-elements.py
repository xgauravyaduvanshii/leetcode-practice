# LeetCode 2567. Minimum Score by Changing Two Elements — Medium
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Submission 2205071834 — Accepted, Python3
#
# My thinking: after sorting, changing two elements can only
# shrink the range from the ends. The best you can do is drop
# the two smallest, the two largest, or one from each end —
# whichever leaves the smallest max-minus-min.
class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min(nums[-1] - nums[2], nums[-3] - nums[0], nums[-2] - nums[1])
