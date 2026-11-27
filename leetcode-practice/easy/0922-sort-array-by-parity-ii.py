# LeetCode 922. Sort Array By Parity II — Easy
# https://leetcode.com/problems/sort-array-by-parity-ii/
# Submission 2197542589 — Accepted, Python3
#
# My thinking: even numbers belong on even positions
# and odd numbers on odd positions. I keep two
# pointers — one for the next free even slot, one
# for the next free odd slot — and drop each
# number into the right kind of slot as I go.

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        even = 0
        odd = 1
        for num in nums:
            if num % 2 == 0:
                result[even] = num
                even += 2
            else:
                result[odd] = num
                odd += 2
        return result
