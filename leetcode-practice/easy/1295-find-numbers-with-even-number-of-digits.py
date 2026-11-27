# LeetCode 1295. Find Numbers with Even Number of Digits — Easy
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Submission 2197568011 — Accepted, Python3
#
# My thinking: I turn each number into a string and
# count its characters — if the length is even, it
# counts. Simple and clear.

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)
