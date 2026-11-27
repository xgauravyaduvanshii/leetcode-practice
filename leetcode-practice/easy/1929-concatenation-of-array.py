# LeetCode 1929. Concatenation of Array — Easy
# https://leetcode.com/problems/concatenation-of-array/
# Submission 2197283807 — Accepted, Python3
#
# My thinking: the answer is just the array written
# twice, back to back. Adding the list to itself
# does exactly that.

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
