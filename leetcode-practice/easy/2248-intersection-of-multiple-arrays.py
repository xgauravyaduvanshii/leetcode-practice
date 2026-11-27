# LeetCode 2248. Intersection of Multiple Arrays — Easy
# https://leetcode.com/problems/intersection-of-multiple-arrays/
# Submission 2197619826 — Accepted, Python3
#
# My thinking: I start with the first array as a set
# and keep only the numbers that also appear in each
# following array. The survivors, sorted, are the
# intersection.

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        common = set(nums[0])
        for arr in nums[1:]:
            common &= set(arr)
        return sorted(common)
