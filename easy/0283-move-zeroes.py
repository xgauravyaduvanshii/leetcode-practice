# LeetCode 283. Move Zeroes — Easy
# https://leetcode.com/problems/move-zeroes/
# Submission 2197461532 — Accepted, Python3
#
# My thinking: I do it in two passes, in place. First
# I slide every non-zero number forward, keeping
# their order, and remember where the next one goes.
# Then I fill everything after that spot with zeros.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
