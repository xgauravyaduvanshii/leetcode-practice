# LeetCode 2239. Find Closest Number to Zero — Easy
# https://leetcode.com/problems/find-closest-number-to-zero/
# Submission 2197619439 — Accepted, Python3
#
# My thinking: I keep the best number seen so far. A
# new number replaces it when it is closer to zero,
# or when it is equally close but positive — ties
# go to the larger number.

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        best = nums[0]
        for x in nums[1:]:
            if abs(x) < abs(best) or (abs(x) == abs(best) and x > best):
                best = x
        return best
