# LeetCode 709. To Lower Case — Easy
# https://leetcode.com/problems/to-lower-case/
# Submission 2197521538 — Accepted, Python3
#
# My thinking: the whole job is turning every
# uppercase letter into lowercase. Python's lower()
# does exactly that, one call.

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
