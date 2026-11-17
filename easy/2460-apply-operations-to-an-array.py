# LeetCode 2460. Apply Operations to an Array — Easy
# https://leetcode.com/problems/apply-operations-to-an-array/
# Submission 2197788889 — Accepted, Python3
#
# My thinking: I scan the array left to right; when
# two neighbours are equal, I double the first and
# zero the second. Then I move all the non-zero
# numbers to the front, keeping their order, and
# fill the rest with zeros.

class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        res = [x for x in nums if x != 0]
        res += [0] * (n - len(res))
        return res
