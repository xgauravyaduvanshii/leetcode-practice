# LeetCode 2367. Number of Arithmetic Triplets — Easy
# https://leetcode.com/problems/number-of-arithmetic-triplets/
# Submission 2197775040 — Accepted, Python3
#
# My thinking: for each number x I check whether x +
# diff and x + 2 * diff are also in the array — that
# makes a triplet. A set makes the lookups quick.

class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        s = set(nums)
        return sum(1 for x in nums if x + diff in s and x + 2 * diff in s)
