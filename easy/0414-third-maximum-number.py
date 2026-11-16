# LeetCode 414. Third Maximum Number — Easy
# https://leetcode.com/problems/third-maximum-number/
# Submission 2197473471 — Accepted, Python3
#
# My thinking: duplicates do not count, so I take
# the distinct numbers, sort them biggest first,
# and pick the third one. If there are fewer than
# three distinct numbers, the answer is the biggest.

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        distinct = sorted(set(nums), reverse=True)
        if len(distinct) >= 3:
            return distinct[2]
        return distinct[0]
