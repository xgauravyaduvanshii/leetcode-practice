# LeetCode 1. Two Sum — Easy
# https://leetcode.com/problems/two-sum/
# Submission 2197267353 — Accepted, Python3
#
# My thinking: for every number, I just need the other number
# that adds up to the target. So I keep the numbers I have
# already seen in a dictionary, with their index. If the
# number I need is already there, I have my answer.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # number -> its index, for the numbers seen so far
        seen_numbers = {}

        for index, number in enumerate(nums):
            needed = target - number

            # did we see the other half before?
            if needed in seen_numbers:
                return [seen_numbers[needed], index]

            # otherwise remember this one and move on
            seen_numbers[number] = index

        # the problem says there is always one answer,
        # this is just here so the function always returns something
        return []
