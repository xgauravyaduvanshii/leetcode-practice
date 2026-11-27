# LeetCode 747. Largest Number At Least Twice of Others — Easy
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# Submission 2197524666 — Accepted, Python3
#
# My thinking: I find the biggest number and where
# it sits. Then I check it against every other
# number — if any of them is more than half of it,
# the biggest is not dominant and the answer is
# -1. Otherwise I return its position.

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = max(nums)
        max_idx = nums.index(max_val)
        for num in nums:
            if num != max_val and max_val < 2 * num:
                return -1
        return max_idx
