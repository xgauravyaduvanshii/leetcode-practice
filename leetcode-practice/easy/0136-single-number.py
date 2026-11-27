# LeetCode 136. Single Number — Easy
# https://leetcode.com/problems/single-number/
# Submission 2197444037 — Accepted, Python3
#
# My thinking: XOR is perfect here — a number XORed
# with itself is 0, and 0 XORed with a number is that
# number. So every pair cancels itself out, and the
# one number left standing is the answer.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer
