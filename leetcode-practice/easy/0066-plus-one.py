# LeetCode 66. Plus One — Easy
# https://leetcode.com/problems/plus-one/
# Submission 2197281305 — Accepted, Python3
#
# My thinking: start from the last digit and add one.
# If it is not 9, I am done. If it is 9 it becomes 0
# and the carry moves left. If every digit was 9,
# I need a new 1 at the front.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
