# LeetCode 217. Contains Duplicate — Easy
# https://leetcode.com/problems/contains-duplicate/
# Submission 2197452317 — Accepted, Python3
#
# My thinking: if I put all the numbers in a set, any
# duplicates collapse into one entry. So if the set
# is smaller than the original list, there must have
# been a duplicate.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
