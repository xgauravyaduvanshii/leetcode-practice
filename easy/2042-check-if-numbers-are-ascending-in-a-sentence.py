# LeetCode 2042. Check if Numbers Are Ascending in a Sentence — Easy
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
# Submission 2197610221 — Accepted, Python3
#
# My thinking: I pull out the numbers in the order
# they appear and check that each one is strictly
# bigger than the one before it. Words are ignored.

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for token in s.split():
            if token.isdigit():
                num = int(token)
                if num <= prev:
                    return False
                prev = num
        return True
