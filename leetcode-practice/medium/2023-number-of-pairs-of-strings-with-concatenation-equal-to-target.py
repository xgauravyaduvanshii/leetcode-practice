# LeetCode 2023. Number of Pairs of Strings With Concatenation Equal to Target — Medium
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/
# Submission 2197609531 — Accepted, Python3
#
# My thinking: I try every ordered pair of different
# indices and count the pairs whose two strings,
# glued together, equal the target.

class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    count += 1
        return count
