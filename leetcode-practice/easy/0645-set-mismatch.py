# LeetCode 645. Set Mismatch — Easy
# https://leetcode.com/problems/set-mismatch/
# Submission 2197509534 — Accepted, Python3
#
# My thinking: I walk through the numbers and note
# which ones I have seen. The first number I see
# twice is the duplicate. The missing number is
# the one from 1 to n that never showed up.

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        duplicate = -1
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        missing = (set(range(1, len(nums) + 1)) - seen).pop()
        return [duplicate, missing]
