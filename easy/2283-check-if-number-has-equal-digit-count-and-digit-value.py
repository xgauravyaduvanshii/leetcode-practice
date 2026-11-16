# LeetCode 2283. Check if Number Has Equal Digit Count and Digit Value — Easy
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
# Submission 2197621481 — Accepted, Python3
#
# My thinking: for each position i, the digit there
# says how many times i should appear in the whole
# number. I check that for every position.

class Solution:
    def digitCount(self, num: str) -> bool:
        for i, ch in enumerate(num):
            if num.count(str(i)) != int(ch):
                return False
        return True
