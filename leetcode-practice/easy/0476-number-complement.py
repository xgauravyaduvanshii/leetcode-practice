# LeetCode 476. Number Complement — Easy
# https://leetcode.com/problems/number-complement/
# Submission 2197480853 — Accepted, Python3
#
# My thinking: I build a mask of all 1s that is as
# long as the number's bits, then XOR with it — that
# flips every bit of the number and nothing else.

class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
