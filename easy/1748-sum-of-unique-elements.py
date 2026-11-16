# LeetCode 1748. Sum of Unique Elements — Easy
# https://leetcode.com/problems/sum-of-unique-elements/
# Submission 2197596863 — Accepted, Python3
#
# My thinking: I count how many times each number
# appears, then add up only the ones that appear
# exactly once.

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        return sum(x for x, c in counts.items() if c == 1)
