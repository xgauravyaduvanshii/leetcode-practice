# LeetCode 2366. Minimum Replacements to Sort the Array — Hard
# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
# Submission 2201699759 — Accepted, Python3
#
# My thinking: I work from the right,
# where the array must already be sorted —
# a number too big for its neighbour gets
# split into as few even pieces as fit,
# and the smallest piece sets the bar for
# the number before it.

class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        ops = 0
        limit = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            x = nums[i]
            if x <= limit:
                limit = x
            else:
                parts = (x + limit - 1) // limit
                ops += parts - 1
                limit = x // parts
        return ops
