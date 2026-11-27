# LeetCode 67. Add Binary — Easy
# https://leetcode.com/problems/add-binary/
# Submission 2197281580 — Accepted, Python3
#
# My thinking: convert both binary strings to numbers,
# add them, and convert the result back to binary.
# The bin() result starts with '0b', so I strip
# the first two characters off.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
