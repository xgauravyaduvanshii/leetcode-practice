# LeetCode 2016. Maximum Difference Between Increasing Elements — Easy
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/
# Submission 2197609204 — Accepted, Python3
#
# My thinking: I walk the array keeping the smallest
# value seen so far. For each new number bigger
# than that minimum, the difference is a candidate
# for the best answer. If no number is ever bigger
# than an earlier one, the answer stays -1.

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        best = -1
        min_seen = nums[0]
        for x in nums[1:]:
            if x > min_seen:
                best = max(best, x - min_seen)
            min_seen = min(min_seen, x)
        return best
