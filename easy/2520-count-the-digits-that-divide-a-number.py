# LeetCode 2520. Count the Digits That Divide a Number — Easy
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Submission 2197798376 — Accepted, Python3
#
# My thinking: I look at each digit of the number
# and count the ones that divide the number evenly.

class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 for ch in str(num) if num % int(ch) == 0)
