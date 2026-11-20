# 3978. Unique Middle Element (Easy)
# https://leetcode.com/problems/unique-middle-element/
# Submission 2200092551 — Accepted, Python3
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        # My thinking: the middle element is the one
        # in the centre of the array. It is unique
        # when it shows up exactly once in total.
        return nums.count(nums[len(nums) // 2]) == 1
