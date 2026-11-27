# LeetCode 541. Reverse String II — Easy
# https://leetcode.com/problems/reverse-string-ii/
# Submission 2197494870 — Accepted, Python3
#
# My thinking: I go through the string in blocks of
# 2k. In each block I reverse only the first k
# characters and leave the rest as they are. The
# slice trick does the reversing for me, and if the
# last block is shorter than k it just reverses
# whatever is left.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(0, len(chars), 2 * k):
            chars[i:i + k] = reversed(chars[i:i + k])
        return "".join(chars)
